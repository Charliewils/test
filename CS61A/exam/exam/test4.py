def decrypt(s, d):
    """List all possible decoded strings of s.
    >>> s = {
    ... 'alan': 'spooky',
    ... 'al': 'drink',
    ... 'antu': 'your',
    ... 'turing': 'ghosts',
    ... 'tur': 'scary',
    ... 'ing': 'skeletons',
    ... 'ring': 'ovaltine'
    ... }
    >>> decrypt('alanturing', s)
    ['drink your ovaltine', 'spooky ghosts', 'spooky scary skeletons']
    """
    if s == '':
        return []
    ms = []
    if d.get(s):
        ms.append(d[s])
    for k in range(1,len(s)):
        first, last = s[:k], s[k:]
        if d.get(first):
            for rest in decrypt(last,d):
                ms.append(d[first] + ' ' + rest)
    return ms


def ensure_consistency(fn):
    """Returns a function that calls fn on its argument, returns fn's
    return value, and returns None if fn's return value is different
    from any of its previous return values for those same argument.
    Also returns None if more than 20 calls are made.
    """
    n = 0
    z ={}
    def helper(x):
        nonlocal n
        n += 1
        if n > 20:
            return None
        val = fn(x)
        if x not in z:
            z[x] = [val]
        if z[x] != [val]:
            return None
        else:
            return val
    return helper


def consistent(x):
        return x

a = ensure_consistency(consistent)
print(a(5))  # Output: 5
print(a(5))  # Output: 5
print(a(6))  # Output: 6
print(a(6))  # Output: 6


lst = [1, 2, 3]

def inconsistent(x):
        return x + lst.pop()

b = ensure_consistency(inconsistent)
print(b(5))  # Output: 8
print(b(5))  # Output: None
print(b(6))  # Output: 7





