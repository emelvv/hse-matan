from math import e, log, sin, sqrt, factorial
import functools
import sys

sys.setrecursionlimit(100000)


@functools.cache
def f(n):

    return (factorial(n)**(1/n))/n


print(round(f(150), 5), e**-1)

