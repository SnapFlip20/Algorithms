# Dijkstra algorithm(heapq)

import heapq
inf = int(1e9)

v, e = 5, 6
start = 1

graph = [[],
         [(2, 2), (3, 3)],
         [(3, 4), (4, 5)],
         [(4, 6)],
         [],
         [(1, 1)]]
visited = [False for _ in range(v+1)]
distance = [inf for _ in range(v+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def test():
    dijkstra(start)
    for i in range(1, v+1):
        if distance[i] == inf:
            print('INF')
        else:
            print(distance[i])

if __name__ == "__main__":
    test()