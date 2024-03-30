# Edmonds Karp

from collections import deque

# ------------------------------------- #
max_v = 100
inf = float('inf')
c = [[0 for _ in range(max_v)] for _ in range(max_v)]
f = [[0 for _ in range(max_v)] for _ in range(max_v)]
adj = [[] for _ in range(max_v)]
s, e = 0, 1
# ------------------------------------- #

def bfs(prev, s, e):
    q = deque([s])
    p = [-1 for _ in range(max_v)]
    while q:
        x = q.popleft()
        for i in adj[x]:
            if c[x][i] - f[x][i] > 0 and p[i] == -1:
                q.append(i)
                p[i] = x
                if i == e:
                    return p

def edmonds_karp(s, e):
    total = 0
    while prev := bfs(s, e):
        flow = inf
        i = e
        while i != s:
            flow = min(flow, c[prev[i]][i]-f[prev[i]][i])
            i = prev[i]
        i = e
        while i != s:
            f[prev[i]][i] += flow
            f[i][prev[i]] -= flow
            i = prev[i]
        total += flow
    
    return total

n = int(input())
m = int(input())
s, e = map(int, input().split())

for i in range(m):
    u, v, w = map(int, input().split()) # u -> v, weight
    c[u][v] = w
    adj[u].append(v)
    adj[v].append(u)

print(edmonds_karp(s, e))
