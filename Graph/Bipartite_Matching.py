# Bipartite Matching

import sys

graph = []

def dfs(a):
    visit[a] = True
    for b in graph[a]:
        matching = group_b[b]
        if matching == -1 or not visit[matching] and dfs(matching):
            group_a[a] = b
            group_b[b] = a
            return True
    return False

n, m = map(int, sys.stdin.readline().split())

for i in range(n):
    s, *tmp = map(int, sys.stdin.readline().split())
    graph.append(tmp)

match = 0
group_a = [-1 for _ in range(n+1)]
group_b = [-1 for _ in range(m+1)]

for i in range(n):
    if group_a[i] == -1:
        visit = [False for _ in range(n)]
        if dfs(i):
            match += 1

print(match)
