# Dijkstra

from heapq import heappush, heappop
inf = int(1e9)

def dijkstra(v, start):
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dist, now = heappop(pq)
        if distance[now] < dist:
            continue
        for (nxt, dist_nxt) in graph[now]:
            cost = dist + dist_nxt
            if cost < distance[nxt]:
                distance[nxt] = cost
                near[nxt] = now
                heappush(pq, (cost, nxt))

def traceback():
    array = []
    trace = end
    while trace != start:
        array.append(trace)
        trace = near[trace]
    array.append(start)

    return array[::-1]



v = 5
start, end = 1, 4
graph = [[],
        [(2, 2), (3, 3)],
        [(3, 4), (4, 5)],
        [(4, 6)],
        [],
        [(1, 1)]]
distance = [inf for _ in range(v+1)]
near = [start for _ in range(v+1)] # for traceback

dijkstra(v, start)
print(distance[end] if distance[end] != inf else "INF")

route = traceback()
print(*route, sep = ' -> ')
