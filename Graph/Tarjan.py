# Tarjan

'''
---list---
graph: 노드 간 연결 관계를 나타낸 (유향)그래프
dfsn: 노드의 방문 순서 저장
finished: SCC로 분리된 노드일 경우 True
stack: DFS로 방문한 노드 순으로 push되는 스택, SCC가 만들어졌을 경우 pop
scc_lst: SCC 집합들을 저장
current_scc: SCC 집합에 포함되는 원소를 저장할 때 사용, 이후 scc_lst에 push
---int---
cnt: dfs 함수의 재귀 횟수, dfsn 배열에 방문 순서를 저장할 때 사용
result: 자기자신과 자식 노드들의 dfsn 번호 중 가장 작은 번호 저장
scc_cnt: SCC 집합의 개수(== len(scc_lst)-1)
'''

#import sys
#sys.setrecursionlimit(10**9)

MAX = 10001

graph = [[] for _ in range(MAX)]
dfsn = [0 for _ in range(MAX)]
finished = [False for _ in range(MAX)]
cnt = 0
stack = []
scc_lst = []

def dfs(node):
    global cnt
    cnt += 1
    dfsn[node] = cnt
    stack.append(node)
    
    result = dfsn[node]
    for i in graph[node]:
        if dfsn[i] == 0:
            result = min(result, dfs(i))
        elif not finished[i]:
            result = min(result, dfsn[i])

    if result == dfsn[node]:
        current_scc = []
        while True:
            t = stack.pop()
            current_scc.append(t)
            finished[t] = True
            if t == node:
                break
        current_scc.sort()
        scc_lst.append(current_scc)
    
    return result        

def main():
    v, e = map(int, input().split())
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)

    for i in range(v):
        if dfsn[i] == 0:
            dfs(i)

    scc_lst.sort()

    scc_cnt = len(scc_lst)-1
    print(scc_cnt)
    for i in scc_lst[1:]:
        print(*i)
    
if __name__ == "__main__":
    main()
