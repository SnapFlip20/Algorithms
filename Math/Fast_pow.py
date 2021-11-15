# Fast power

def fast_pow(x, y, mod=None):
    res = 1
    while True:
        if (y == 0):
            break
        if (y % 2 == 1):
            res = (res*x) % mod
        y //= 2
        x = (x**2) % mod

    return res


def fast_pow2(x, y, mod=None):
    res = 1
    x %= mod
    while y > 0:
        if y & 1:
            res = (res * x) % mod
        y >>= 1
        x = x * x % mod
    return res
