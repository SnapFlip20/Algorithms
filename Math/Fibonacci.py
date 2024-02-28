# calculate nth Fibonacci Number

# 1. 재귀 x, 메모이제이션 x, 메모리 사용 최소
def fib(n):
    if n == 1 or n == 2:
        return 1
    fa, fb = 1, 1
    for i in range(1, n):
        fa, fb = fb, fa+fb

    return fa

# 2. 재귀 o, 메모이제이션 x
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
# 3. 재귀 o, 메모이제이션 o (top-down)
memo = {1: 1, 2: 1}
def fib(n):
    if n in memo:
        return memo[n]
    elif n < 2:
        memo[n] = n
        return n
    else:
        fn = fib(n-1) + fib(n-2)
        memo[n] = fn
        return fn
    
# 4. 재귀 o, 캐싱 사용
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 5. 재귀 x, 메모이제이션 o (bottom-up)
def fib(n):
    dp = [0, 1, 1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2])

    return dp[n]

# 6. 행렬 제곱 사용
def matmul(m1, m2):
    mt = []
    for i in range(len(m1)):
        mt.append([])
        for j in range(len(m2[0])):
            tmp = 0
            for k in range(len(m1[0])):
                tmp += m1[i][k]*m2[k][j]
            mt[i].append(tmp)
    return mt

def matpow(m, n):
    if n == 1:
        return m
    else:
        div = matpow(m, n//2)
        if n % 2 == 0:
            return matmul(div, div)
        else:
            return matmul(matmul(div, div), m)

def fib(n):     
    _m = [[1, 1], [1, 0]]
    return (matpow(_m, n)[0][1])

# 7. 일반항
import decimal
from decimal import Decimal
from math import ceil

decimal.getcontext().prec = 10000

def fib(n):
    root5 = Decimal(5).sqrt()
    v = (((1+root5)/2)**n - ((1-root5)/2)**n)
    div = 1/root5
    return ceil(v * div)
