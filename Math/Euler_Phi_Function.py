# Euler Phi(totient) Function
# euler_phi(n) returns number of k that meets GCD(n, k) = 1

def euler_phi(n):
    i, res = 2, n
    while i**2 <= n:
        if n % i == 0:
            res = res - res//i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        res = res - res//n

    return res


n = int(input())

print(euler_phi(n))
