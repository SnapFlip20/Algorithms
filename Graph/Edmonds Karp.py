# Edmonds Karp

from collections import deque

# ------------------------------------- #
max_v = 100
inf = 10**10
c = [[0 for _ in range(max_v)] for _ in range(max_v)]
f = [[0 for _ in range(max_v)] for _ in range(max_v)]
adj = [[] for _ in range(max_v)]
total = 0
flow = inf
s, e = 0, 1
# ------------------------------------- #

def bfs(prev, s, e):
    q = deque()
    q.append(s)
    while q:
        if prev[e] != -1:
            break
        x = q.popleft()
        for i in adj[x]:
            if c[x][i] - f[x][i] > 0 and prev[i] == -1:
                q.append(i)
                prev[i] = x
                if i == e:
                    break
    if prev[e] == -1:
        return True
    else:
        return False

def edmonds_karp(s, e):
    global flow, total
    while True:
        prev = [-1 for _ in range(max_v)]
        if bfs(prev, s, e):
            break
        
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
    c[u][v] = 1
    adj[u].append(v); adj[v].append(u)

print(edmonds_karp(s, e))
