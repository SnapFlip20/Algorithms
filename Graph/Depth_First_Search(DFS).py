# Depth First Search(DFS)

'''
import sys
sys.setrecursionlimit(10**9)
'''
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 1. adjacency list
def dfs_adjlst(v):
    visit[v] = True
    order.append(v)
    for i in graph[v]:
        if not visit[i]:
            dfs_adjlst(i)

# 1-1. adjacency list + calculate distance
def dfs_dist(v):
    visit[v] = True
    for i in graph[v]:
        if not visit[i]:
            dist[i] = dist[v]+1
            dfs_dist(i)

# 2. adjacency matrix / 1-indexed
def dfs_adjmtx(v):
    visit[v] = True
    order.append(v)
    # ok: node visiting condition expression
    ok = 1
    for i in range(1, len(graph)-1):
        if (graph[v][i] == ok and not visit[i]):
            dfs_adjmtx(i)

# 3. dfs in N*M map
def dfs_nm(x, y):
    global m, n
    if 0 <= x < m and 0 <= y < n:
        order.append((x, y))
        # ok: node visiting condition expression
        ok = 1
        if graph[y][x] == ok:
            graph[y][x] = 0
            for (i, j) in zip(dx, dy):
                dfs_nm(x+i, y+i)
            return True
    return False

# 4. dfs in N*N map
def dfs_nn(x, y):
    global n
    if 0 <= x < n and 0 <= y < n:
        order.append((x, y))
        # ok: node visiting condition expression
        ok = 1
        if graph[y][x] == ok:
            graph[y][x] = 0
            for (i, j) in zip(dx, dy):
                dfs_nn(x+i, y+i)
            return True
    return False

# ------------- checking ------------- #

def check_distance_of_nodes(): # 1-indexed
    global visit, graph, dist
    
    # n: number of vertexs / m: number of edges
    n, m = map(int, input().split())
    # s: start node
    s = int(input())

    graph = [[] for _ in range(n+1)] # 1-indexed
    visit = [False for _ in range(n+1)] # 1-indexed
    dist = [0 for _ in range(n+1)]

    # input edges(from, to)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs_dist(s)

    print(f'from {s}')
    for (i, j) in enumerate(dist[1:]):
        if i+1 != s:
            print(f'to {i+1}: {j if j != 0 else "path does not exist"}')

def check_traversal_order():
    global visit, graph, order

    # n: number of vertexs / m: number of edges
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)] # 1-indexed
    visit = [False for _ in range(n+1)] # 1-indexed
    order = []

    # input edges(from, to)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1):
        if not visit[i]:
            dfs_adjlst(i)

    print('traversal order: ', end = '')
    print(*order, sep = ' -> ')

def check_connected_component():
    global visit, graph, order

    # n: number of vertexs / m: number of edges
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)] # 1-indexed
    visit = [False for _ in range(n+1)] # 1-indexed
    order = []

    # input edges(from, to)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    for i in range(1, n+1):
        if not visit[i]:
            dfs_adjlst(i)
            cnt += 1

    print('the number of connected component:', cnt)
    print('traversal order: ', end = '')
    print(*order, sep = ' -> ')

def check_permutation_cycle():
    global visit, graph, order

    # n: number of vertexs
    n = int(input())
    graph = [[] for _ in range(n+1)] # 1-indexed
    visit = [False for _ in range(n+1)] # 1-indexed
    order = []

    # input edges(from, to)
    for i in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)

    cnt = 0
    for i in range(1, n+1):
        if not visit[i]:
            dfs_adjlst(i)
            cnt += 1

    print('the number of permutation cycles:', cnt)
    print('traversal order: ', end = '')
    print(*order, sep = ' -> ')

def adj_to_mtx(adj):
    n = len(adj)-1 # if 0-indexed, -1 is necessary
    # 0: not visited / 1: visited
    mtx = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for (i, j) in enumerate(adj):
        print(i, j)
        for k in j:
            mtx[i][k] = 1

    return mtx

def mtx_to_add(mtx):
    n = len(mtx)
    adj = [[] for _ in range(n+1)] # if 1-indexed, +1 is necessary
    for i in range(n):
        for j in range(n):
            if mtx[i][j] == 1:
                adj[i].append(j)

    return adj



if __name__ == "__main__":
    ...