# from BOJ 10825

import sys

lst = []

n = int(sys.stdin.readline())

'''
input example:
Junkyu 50 60 100
Sangkeun 80 60 50
sunyoung 80 70 100
'''
for i in range(n):
    a, b, c, d = sys.stdin.readline().split()
    lst.append([a, int(b), int(c), int(d)])

new = sorted(lst, key = lambda a: (-a[1], a[2], -a[3], a[0]))
# desc(kor) / asc(eng) / desc(math) / asc(name)

for j in new:
    print(j[0])
