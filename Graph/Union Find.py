# Disjoint set(Weighted Union Find)

def union(a, b):
    if (a := find(a)) == (b := find(b)):
        return
    if tree[a] < tree[b]:
        tree[a] += tree[b]
        tree[b] = a
    else:
        tree[b] += tree[a]
        tree[a] = b

def find(n):
    if tree[n] < 0 :
        return n
    else:
        tree[n] = find(tree[n])
        return tree[n]

v = 100
tree =  [-1 for x in range(v+1)]
