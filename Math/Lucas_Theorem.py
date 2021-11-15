# Lucas Theorem

MAX = 2000

def lucas_theorem(n, k, mod):
    binom = [[0 for _ in range(MAX)] for _ in range(MAX)]
    for i in range(mod):
        binom[i][0] = 1
        for j in range(1, i+1):
            binom[i][j] = (binom[i-1][j-1] + binom[i-1][j]) % mod
        
    res = 1
    while n or k:
        res *= binom[n%mod][k%mod]
        n //= mod
        k //= mod
        res %= mod

    return res

n, k, mod = map(int, input().split())

print(lucas_theorem(n, k, mod))
