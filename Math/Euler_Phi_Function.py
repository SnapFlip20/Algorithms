# Euler Phi(totient) Function
# euler_phi(n) returns number of k that meets GCD(n, k) = 1

def euler_phi(n):
    res = n
    for i in range(2, round(n**0.5)+1):
        if n % i == 0:
            res *= (1 - (1/i))
            while n % i == 0:
                n //= i
    if n == 1:
        return round(res)
    else:
        res *= (1 - (1/n))
        return round(res)

n = int(sys.stdin.readline())

print(euler_phi(n))
