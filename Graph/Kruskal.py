# Kruskal

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

v, e = map(int, input().split())
tree = {x:x for x in range(v+1)}
graph = []

for i in range(e):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

graph.sort(key = lambda x: x[2])

weight = 0
for i in graph:
    a, b, c = i
    if find(a) != find(b):
        union(a, b)
        weight += c

print(weight)
