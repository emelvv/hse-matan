from fractions import Fraction
from math import sqrt, sin, factorial, pi

F = Fraction


def f(n):
    return sin(pi*(n**3+1)**(1/3))


# for n in range(2, 1000):
#     if f(n) > h(n):
#         print(n)
print(round(f(5000), 5))
