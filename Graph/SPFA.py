# Shortest Path Faster Algorithm(SPFA)

from collections import deque

INF = 10**9

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]
isinQueue = [0 for _ in range(n+1)]
isInfCycle = [0 for _ in range(n+1)]

def spfa(start):
    dist[start] = 0
    isinQueue[start] = 1
    q = deque(); q.append(start)
    while q:
        now = q.popleft()
        isinQueue[now] = 0
        for nxt, cost in graph[now]:
            if dist[nxt] > dist[now]+cost:
                dist[nxt] = dist[now]+cost
                if isinQueue[nxt] == 0:
                    isInfCycle[nxt] += 1
                    if isInfCycle[nxt] >= n: # negative cycle
                        return True
                    isinQueue[nxt] = 1
                    q.append(nxt)
    return False

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start = int(input())
spfa(start)