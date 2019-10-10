import random

"""
max_inversions = (n * (n - 1)) / 2

O(f(n)) = n * log n
"""

ls = [x for x in range(10)]
random.shuffle(ls)


def countInverisons(A):
    if len(A) == 1:
        return A, 0
    
    ln = len(A) // 2
    b, x = countInverisons(A[:ln])
    c, y = countInverisons(A[ln:])

    d, z = CountSplit(A, b, c)
    return d, (x+y+z)

def CountSplit(A, b, c):
    count = 0
    i, j = 0, 0
    res = []

    while i < len(b) and j < len(c):
        if b[i] < c[j]:
            res.append(b[i])
            i += 1
        else:
            if c[j] < b[i]:
                res.append(c[j])
                j += 1
                count += (len(b) - i)
    res += b[i:]
    res += c[j:]
    return res, count


print('ls before', ls)
a, b = countInverisons(ls)
print('ls after', b, 'array', a)

