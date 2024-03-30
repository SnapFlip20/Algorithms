# find next pow of 2
# if n is pow of 2, return n
# f(4) = 4 / f(25) = 32 / f(513) = 1024

def find_next2pow(n):
    if n < 1:
        return 1
    n -= 1
    while n & n-1:
        n = n&n - 1
    return n<<1
