# Lowest Common Ancestor(LCA)

from collections import deque

log = 20 # m < 2**log

def bfs(root_node): # check each node's depth
    check[root_node] = 1
    q = deque([root_node])
    while q:
        now_node = q.popleft()
        for next_node in graph[now_node]:
            if check[next_node]:
                continue
            depth[next_node] = depth[now_node] + 1
            check[next_node] = 1
            parent[next_node][0] = now_node
            q.append(next_node)

def make_tree(): # make tree(using DP table)
    bfs(1)
    for j in range(1, log):
        for i in range(1, n+1):
            parent[i][j] = parent[parent[i][j-1]][j-1]

def lca(x, y): # find lowest common ancestor
    if depth[x] > depth[y]:
        x, y = y, x
    for i in range(log-1, -1, -1):
        if depth[y] - depth[x] >= (1 << i):
            y = parent[y][i]
    if x == y:
        return x
    for i in range(log-1, -1, -1):
        if parent[x][i] != parent[y][i]:
            x = parent[x][i]
            y = parent[y][i]
    return parent[x][0]

n = int(input()) # node

graph = [[] for _ in range(n+1)]
check = [0 for _ in range(n+1)]
depth = [0 for _ in range(n+1)]
parent = [[0 for x in range(log)] for y in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

make_tree()

m = int(input())

for _ in range(m):
    x, y = map(int, input().split()) # two vertex
    print(lca(x, y))
