# Topology sort for DAG

from collections import deque

v, e = map(int, input().split())
ind = [0 for _ in range(v+1)] # indegree
graph = [[] for _ in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    ind[b] += 1

res = []
def TopologySort():
    q = deque()
    for i in range(1, v+1):
        if ind[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        res.append(node)
        for i in graph[node]:
            ind[i] -= 1
            if ind[i] == 0:
                q.append(i)

TopologySort()

print(*res)
