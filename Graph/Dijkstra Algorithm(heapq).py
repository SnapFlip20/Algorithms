# dijkstra algorithm(heapq)

import heapq, sys

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

# 다익스트라 알고리즘 수행
def dijkstra(start):
    q = []
    # 최소 힙 내부의 튜플 형태: (거리, 노드), 거리 순으로 정렬됨
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 빌 때까지
        dist, now = heapq.heappop(q) # 최단 거리가 가장 짧은 노드 정보 반환
        
        if distance[now] < dist: # 이미 처리된 노드일 경우 무시
            continue

        for i in graph[now]:
            cost = dist + i[1]
            
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == inf: # 도달할 수 없는 경우
        print('INF')
    else: # 도달할 수 있는 경우
        print(distance[i])

