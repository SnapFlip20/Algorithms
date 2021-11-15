# Disjoint set(Union Find)

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

n = int(input())
tree = {x:x for x in range(n+1)}
m = int(input())

# union
for i in range(m):
    a, b = map(int, input().split())
    union(a, b)

# find
for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print('O')
    else:
        print('X')
