# Cooley-Tukey algorithm for Fast Fourier Transform

from cmath import exp, pi

def fft(f):
    n = len(f)
    if n <= 1: return f
    even = fft(f[0::2])
    odd = fft(f[1::2])
    _f = [exp((2j*k*pi)/n)*odd[k] for k in range(n//2)]
    return [even[x]+_f[x] for x in range(n//2)]+[even[x]-_f[x] for x in range(n//2)]

def ifft(f):
    n = len(f)
    if n <= 1: return f
    even = ifft(f[0::2])
    odd = ifft(f[1::2])
    _f = [exp((-2j*k*pi)/n)*odd[k] for k in range(n//2)]
    return [even[x]+_f[x] for x in range(n//2)]+[even[x]-_f[x] for x in range(n//2)]
