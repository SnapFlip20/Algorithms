# Chinese Remainder Theorem

from functools import reduce

def modinv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while (a > 1):
        q = a // b
        a, b = b, a%b
        x0, x1 = x1-q*x0, x0
    if x1 < 0:
        x1 += b0
    return x1

def CRT(n, a):
    s = 0
    product = reduce(lambda a, b: a*b, n)
    for (ni, ai) in zip(n, a):
        p = product // ni
        s += ai*modinv(p, ni)*p
    return s % product

n = [3, 5, 7]
a = [2, 3, 2]

print(CRT(n, a))

