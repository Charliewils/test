def accumulate(lst):
    """
    >>> deep = [3, 7, [2, 5, 6], 9]
    >>> accumulate(deep)
    32
    >>> deep
    [3, 10, [2, 7, 13], 32]
    """
    count = 0
    for i in range(len(lst)):
        if not isinstance(lst[i],list):
            count += lst[i]
            lst[i] = count
        else:
            count += accumulate(lst[i])
    return count

