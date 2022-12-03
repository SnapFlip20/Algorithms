# Bellman Ford

INF = 10**9

n, m = map(int, input().split())
graph = []
dist = [INF for _ in range(n+1)]

def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            now, nxt, cost = graph[j]
            if dist[now] != INF and dist[nxt] > dist[now]+cost:
                dist[nxt] = dist[now]+cost
                if i == n-1: # check negative cycle
                    return True
    return False        

for i in range(m):
    u, v, w = map(int, input().split())
    graph.append((u, v, w))

start = int(input())
bellman_ford(start)