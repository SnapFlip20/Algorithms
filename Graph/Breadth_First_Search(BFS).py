# Breadth First Search(BFS)


# 1. 기본형
from collections import deque

def bfs(graph, start, visit):
    q = deque([start])
    visit[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visit[i]:
                q.append(i)
                visit[i] = True

# 0. 테스트용
def _bfs(graph, start, visit):
    q = deque([start])
    visit[start] = True
    while q:
        v = q.popleft()
        print(v)
        for i in graph[v]:
            if not visit[i]:
                q.append(i)
                visit[i] = True

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
    _bfs(graph, 1, visit)

if __name__ == "__main__":
    test()
