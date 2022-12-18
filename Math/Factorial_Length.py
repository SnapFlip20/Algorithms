# Find the length of factorial of a number
# log10(n!) = log10(1) + log10(2) + log10(3) + ... + log10(n)

from math import log10

def factorial_length(n):
    res = 0
    for j in range(n, 0, -1):
        res += log10(j)
    return int(res)+1
