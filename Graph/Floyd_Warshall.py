# Floyd Warshall

inf = int(1e9)

v, e = 5, 14

graph = [[inf, inf, inf, inf, inf, inf],
         [inf, 0, 2, 3, 1, 10],
         [inf, inf, 0, inf, 2, inf],
         [inf, 8, inf, 0, 1, 1],
         [inf, inf, inf, inf, 0, 3],
         [inf, 7, 4, inf, inf, 0]]

def floyd_warshall():
    for k in range(1, v+1):
        for a in range(1, v+1):
            for b in range(1, v+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

def test():
    floyd_warshall()

    for i in range(1, v+1):
        for j in range(1, v+1):
            if graph[i][j] == inf:
                graph[i][j] = 0
        print(*graph[i][1:])

if __name__ == "__main__":
    test()