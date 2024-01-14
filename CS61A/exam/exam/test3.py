def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch) "Must be a Tree"
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(branch):
    if type(branch) != list or len(branch) < 1:
        return False
    for t in branches(branch):
        if not is_tree(t):
            return False
    return True

def is_leave(branch):
    return not branches(branch)



def sum_range(t):
    """Returns the range of the sums of t, that is, the
    difference between the largest and the smallest
    sums of t."""
    def helper(t):
        if is_leave(t):
            return [label(t),label(t)]
        else:
            a = min(helper(b)[1] for b in branches(t))
            b = max(helper(b)[0] for b in branches(t))
            x = label(t)
            return [b+x,a+x]
    x, y = helper(t)
    return x-y
