# Union Find Algorithm

import sys

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        tree[b] = a
    else:
        tree[a] = b

def find(n):
    if tree[n] == n:
        return n
    else:
        tree[n] = find(tree[n])
        return tree[n]

n = int(sys.stdin.readline())
tree = {x:x for x in range(n+1)}
m = int(sys.stdin.readline())

# union
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

# find
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        print('O')
    else:
        print('X')
