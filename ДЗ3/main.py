# from math import sqrt
import functools
import sys

sys.setrecursionlimit(100000)


@functools.cache
def f(n):
    if n == 1:
        return 3
    return f(n-1)**2-2


@functools.cache
def g(n):
    mul = 1
    for i in range(1, n):
        mul *= f(i)
    return f(n)/(mul)


print(round(g(10), 10), 5**0.5)
