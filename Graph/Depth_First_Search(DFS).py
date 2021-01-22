# Depth First Search(DFS)

def dfs(graph, v, visit):
    visit[v] = True
    print(v)
    for i in graph[v]:
        if not visit[i]:
            dfs(graph, i, visit)

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
    dfs(graph, 1, visit)

if __name__ == "__main__":
    _test()
