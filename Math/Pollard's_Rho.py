# Pollard's Rho Algorithm

import sys
from math import gcd, sqrt
from random import randrange

def MillerRabin(num, prime):
    s = num-1
    cnt = 0
    while s & 1 == 0:
        s >>= 1
        cnt += 1
    p = pow(prime, s, num)
    if p == 1 or p == num-1:
        return True
    for i in range(cnt-1):
        p = pow(p, 2, num)
        if p == num-1:
            return True
    return False

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
   
def isPrime(x):
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if x in primeList:
        return True
    for i in primeList:
        if not MillerRabin(x, i):
            return False
    return True
