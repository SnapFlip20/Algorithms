# Traveling Salesman Problem

n = int(input())
w = []
inf = int(1e10)
dp = [[-1 for _ in range(1<<n)] for _ in range(n)]

for i in range(n):
    w.append(list(map(int, input().split())))
    
def tsp(current, visit):
    if visit == (1<<n)-1:
        if w[current][0] != 0:
            return w[current][0]
        else:
            return inf
        
    if dp[current][visit] != -1:
        return dp[current][visit]
    
    ret = inf
    for nxt in range(n):
        if visit & (1<<nxt):
            continue
        if w[current][nxt] == 0:
            continue
        ret = min(ret, tsp(nxt, visit|(1<<nxt)) + w[current][nxt])
    dp[current][visit] = ret
    return ret

print(tsp(0, 1))
