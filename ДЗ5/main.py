from fractions import Fraction
from math import cos, pi
F = Fraction


def seq(n):
    sequence = []
    for k in range(1, n):
        sequence.append(1 + 2*(-1)**(k+1)+3*(-1)**((k*(k-1))/2))

    return sequence


lst = seq(99)


def M(n):
    return max(lst[n:])


def m(n):
    return min(lst[n:])


for n in range(1, 55):
    print(n, m(n))
