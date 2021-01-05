# Fast power algorithm 2

def fast_pow2(x, y, mod=None):
    res = 1
    x %= mod
    while y > 0:
        if y & 1:
            res = (res * x) % mod
        y >>= 1
        x = x * x % mod
    return res

x, y = map(int, input('밑과 지수를 입력하세요: ').split())
mod = int(input('나머지를 입력하세요: '))

print(fast_pow2(x, y, mod))
