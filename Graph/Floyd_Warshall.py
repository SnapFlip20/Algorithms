# Floyd Warshall Algorithm

import sys

inf = int(1e9)

n = int(sys.stdin.readline()) # 노드의 개수
m = int(sys.stdin.readline()) # 간선의 개수

graph = [[inf for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == inf:
            graph[i][j] = 0
    print(*graph[i][1:])
