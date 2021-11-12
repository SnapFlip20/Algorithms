# Depth First Search(DFS)


'''
import sys
sys.setrecursionlimit(10**9)
'''

# 1. 기본형(graph가 인접 행렬)
def dfs(graph, v, visit):
    n = len(graph)
    visit[v] = True
    for i in range(1, n+1):
        if (graph[v][i] == 1 and not visit[i]):
            dfs(graph, i, visit)

# 2. 기본형(graph가 인접 리스트)
def dfs(graph, v, visit):
    visit[v] = True
    for i in graph[v]:
        if not visit[i]:
            dfs(graph, i, visit)

# 3. NxM 크기의 map에서 기본형
graph = []
def dfs(x, y):
    global m, n
    if x < 0 or y < 0 or x >= m or y >= n: # 범위를 벗어나면
        return False
    if graph[y][x] == 1: # 아직 방문하지 않았다면
        graph[y][x] = 0
        # 재귀함수 호출
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

# 4. NxN 크기의 map에서 연결된 구역의 개수와 넓이를 알고 싶을 때
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
matrix_nn = [[1, 1, 0, 1],
             [0, 0, 0, 1],
             [0, 1, 1, 1],
             [0, 0, 1, 0]]
n = 4
 
def dfs(x, y):
    global cnt
    matrix_nn[x][y] = 0
    cnt += 1
    for k in range(4) :
        ddx, ddy = x + dx[k], y + dy[k]
        if ddx < 0 or ddx >= n or ddy < 0 or ddy >= n:
            continue
        if matrix_nn[ddx][ddy] == 1 :
            dfs(ddx,ddy)

def check():
    global cnt
    lst = []
    for i in range(n):
        for j in range(n):
            if matrix_nn[i][j] == 1:
                cnt = 0
                dfs(i, j)
                lst.append(cnt)
    print('구역의 개수:', len(lst))
    print(*lst)

# 0. 테스트용
def _dfs(graph, v, visit):
    visit[v] = True
    print(v)
    for i in graph[v]:
        if not visit[i]:
            _dfs(graph, i, visit)

def test():
    '''
         <예시 그래프>

               1 ⟹ 시작
             ╱ │ ╲
            2  4  8
           ╱  ╱ ╲
          5  3   7
                ╱
               6
    
    '''
    graph = [
        [],
        [2, 4, 8],
        [1, 5],
        [4],
        [1, 3, 7],
        [2],
        [7],
        [4, 6],
        [1]
    ]
    visit = [False for i in range(9)]
    print('노드 방문 순서:')
    _dfs(graph, 1, visit)

if __name__ == "__main__":
    test()
