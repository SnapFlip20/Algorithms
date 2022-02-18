# Pollard's Rho Algorithm

from math import gcd
from random import randrange

def PollardRho(num):
    if isPrime(num):
        return num
    if num == 1:
        return num
    if num % 2 == 0:
        return 2
    x = y = randrange(2, num)
    c = randrange(1, num)
    f = lambda x: (pow(x, 2, num) + c + num) % num
    d = 1
    while d == 1:
        x, y = f(x), f(f(y))
        d = gcd(abs(x-y), num)
        if d == num:
            return PollardRho(num)
    if isPrime(d):
        return d
    else:
        return PollardRho(d)
