# Monotone Chain

import sys

def ccw(cd1, cd2, cd3):
    x1, y1 = cd1; x2, y2 = cd2; x3, y3 = cd3
    return (x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)

def monotone_chain(cd):
    u = []; l = [];
    cd.sort()
    for i in cd:
        while len(u) > 1 and ccw(u[-2], u[-1], i) <= 0:
            u.pop()
        u.append(i)
        while len(l) > 1 and ccw(l[-2], l[-1], i) >= 0:
            l.pop()
        l.append(i)
    return u, l

n = int(input())

cd = []

for i in range(n):
    x, y = map(int, input().split())
    cd.append((x, y))

upper, lower = monotone_chain(cd)

print(len(upper) + len(lower) - 2)
