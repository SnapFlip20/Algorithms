# GCD
def extgcd(a, b):
    if b != 0:
        x = extgcd(b, a%b)
        return (x[1], x[0]-(a//b)*x[1])
    else:
        return (1, 0)

# Modular Inverse
def modinv(a, mod):
    return (extgcd(a, mod)[0]+mod) % mod
