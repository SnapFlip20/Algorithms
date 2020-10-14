# Fast power algorithm(divide and conquer)

'''
빠른 거듭제곱 구하기

분할 정복 알고리즘을 이용하여 거듭제곱을 빠르게 구할 수 있는데,
예를 들면 2**8을 (2**4)*(2**4) -> ((2**2)(2**2))*((2**2)(2**2))로 분할하여 곱하는 것이다.
단, 2**5처럼 지수가 홀수일 때는 (2**2)*(2**3)로 분할한다.

아래 fast_pow() 함수의 시간복잡도는 O(logN)이다.
'''

def fast_pow(x, y, mod=None):
    res = 1
    while True:
        if (y == 0):
            break
        if (y % 2 == 1): # if y is odd
            res = (res*x) % mod
        y //= 2
        x = (x**2) % mod

    return res

x, y = map(int, input('밑과 지수를 입력하세요: ').split())
mod = int(input('나머지를 입력하세요: '))

print(fast_pow(x, y, mod))
