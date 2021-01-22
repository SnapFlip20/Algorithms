# Breadth First Search(BFS)

from collections import deque

def bfs(graph, start, visit):
    q = deque([start])
    visit[start] = True
    while q:
        v = q.popleft()
        print(v)
        for i in graph[v]:
            if not visit[i]:
                q.append(i)
                visit[i] = True

def _test():
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]
    visit = [False for i in range(9)]
    bfs(graph, 1, visit)

if __name__ == "__main__":
    _test()
