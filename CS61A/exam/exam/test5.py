class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            rest_expr = ', ' + repr(self.branches)
        else:
            rest_expr = ''
        return "Tree({0}{1})".format(self.label, rest_expr)

    def is_leave(self):
        return not self.branches

class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_expr = ', ' + repr(self.rest)
        else:
            rest_expr = ''
        return "Link({0}{1})".format(self.first, rest_expr)

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]


def linky_paths(t):
    """
    >>> t = Tree(1, [Tree(2)])
    >>> linky_paths(t)
    >>> t
    Tree(Link(1), [Tree(Link(2, Link(1)))])
    """
    def helper(t, path_so_far):
        t.label = Link(t.label, path_so_far)
        for branch in t.branches:
            return helper(branch, t.label)
    return helper(t, Link.empty)

def find_file_path(t, file_str):
    """
    >>> t = Tree('data', [Tree('comm', [Tree('dummy.py')]),Tree('ecc',[Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])
    >>> find_file_path(t, 'file2.py')
    '/data/file2.py'
    >>> find_file_path(t, 'dummy.py')
    '/data/comm/dummy.py'
    >>> find_file_path(t, 'hello.py')
    '/data/ecc/hello.py'
    >>> find_file_path(t, 'file.py')
    '/data/ecc/file.py'
    """
    def helper(t, file_str, path_so_far):
        path = path_so_far + '/' + t.label
        if t.label == file_str:
            return path
        elif t.is_leave():
            return None
        for branch in t.branches:
            result = helper(branch, file_str, path)
            if result:
                return result
    
    return helper(t, file_str, '')

def convert_to_string(link):
    """
    >>> link = Link('data', Link('file2.py'))
    >>> convert_to_string(link)
    '/data/file2.py'
    """
    if link.rest:
        return '/' + link.first + convert_to_string(link.rest)
    return '/' + link.first

def all_paths(t):
    """
    >>> t1 = Tree(1, [Tree(2), Tree(3)])
    >>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)])])
    >>> all_paths(t1)
    [Link(1, Link(2)), Link(1, Link(3))]
    >>> all_paths(t2)
    [Link(1, Link(2)), Link(1, Link(3, Link(4))), Link(1, Link(3, Link(5)))]
    """
    if t.is_leave():
        return [Link(t.label)]
    result = []
    for branch in t.branches:
        result.extend([Link(t.label, branch) for branch in all_paths(branch)])
    return result

def find_file_path2(t, file_str):
    """
    >>> t = Tree('data', [Tree('comm', [Tree('dummy.py')]), Tree('ecc', [Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])
    >>> find_file_path2(t, 'file2.py')
    '/data/file2.py'
    >>> find_file_path2(t, 'dummy.py')
    '/data/comm/dummy.py'
    >>> find_file_path2(t, 'hello.py')
    '/data/ecc/hello.py'
    >>> find_file_path2(t, 'file.py')
    '/data/ecc/file.py'
    """
    for link in all_paths(t):
        original = convert_to_string(link)
        while link is not Link.empty:
            if link.first == file_str:
                return original
            link = link.rest
    return None

def skip(lnk, n):
    """
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> skip(lnk, 2)
    >>> lnk
    Link(1, Link(3, Link(5)))
    >>> lnk2 = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> skip(lnk2, 4)
    >>> lnk2
    Link(1, Link(2, Link(3, Link(5, Link(6)))))
    """
    def skipper(lst):
        nonlocal count
        count += 1
        if lst is Link.empty:
            return 
        elif count == n-1:
            lst.rest = lst.rest.rest
            count = 0
        return skipper(lst.rest) 
    count = 0
    return skipper(lnk)
   
