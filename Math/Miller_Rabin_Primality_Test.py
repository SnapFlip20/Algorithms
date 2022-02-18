# Miller Rabin Primality Test

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
