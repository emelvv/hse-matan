from fractions import Fraction
F = Fraction

# def f1(x, n):
#     s=0
#     for k in range(0, n+1):
#         s+=x**k
#     return s

# def f2(x, n):
#     return F((x**(n+1)-1),(x-1))

# print(f1(F(1,3), 5), f2(F(1,3), 5))

def f1(n):
    s=0
    for k in range(1, n+1):
        s+=F(5*3**k-3, 6)
    return s

def f2(n):
    return F(5*3**n-2*n-5, 4)

print(f1(10), f2(10))
