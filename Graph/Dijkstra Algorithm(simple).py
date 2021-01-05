# Dijkstra algorithm

import sys

inf = int(1e9)

print('노드의 개수, 간선의 개수 순서대로 입력:')
n, m = map(int, sys.stdin.readline().split()) # 노드의 개수, 간선의 개수

print('시작 노드 번호 입력:')
start = int(sys.stdin.readline()) # 시작 노드 번호

graph = [[] for i in range(n+1)] # 노드 연결 정보를 담는 리스트

visited = [False] * (n+1) # 방문 여부를 체크하는 리스트

distance = [inf] * (n+1) # 최단 거리 테이블을 모두 inf로 초기화

print('a번 노드->b번 노드, 비용: c일 때 a, b, c를 순서대로 입력:')
for i in range(m): # 모든 간선 정보를 입력받기
    a, b, c = map(int, sys.stdin.readline().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호 리턴
def get_smallest_node():
    min_value = inf
    index = 0 # 가장 최단 거리가 짧은 노드
    for i in range(1, n+1):
        if (distance[i] < min_value) and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘 수행
def dijkstra(start):
    distance[start] = 0 # 시작 노드 초기화
    visited[start] = True # 방문 처리
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1): # 시작 노드를 제외한 전체 (n-1)개의 노드에 대해 반복
        now = get_smallest_node() # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문 처리
        visited[now] = True
        for j in graph[now]: # 현재 노드와 연결된 다른 노드 확인
            cost = distance[now] + j[1]
            if cost < distance[j[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧으면
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == inf: # 도달할 수 없는 경우
        print('INF')
    else: # 도달할 수 있는 경우
        print(distance[i])

