# Gale-Shapley Algorithm for Stable Matching Problem

n = 4
matched_w = [0 for _ in range(n+1)]
matched_m = [0 for _ in range(n+1)]
fail = [[0 for _ in range(n)] for _ in range(n)]
prefer_lst = [[3, 2, 1, 4],
              [2, 4, 1, 3],
              [3, 1, 4, 2],
              [1, 2, 3, 4], 
              [1, 3, 2, 4],
              [3, 4, 2, 1],
              [2, 3, 4, 1],
              [4, 2, 1, 3]]

while not all(matched_w[1:]):
    for i in range(n):
        if matched_m[i+1]:
            continue
        for j in range(n):
            if fail[i][j] == 1:
                continue
            propose = prefer_lst[i][j]
            if matched_w[propose] == 0:
                matched_w[propose] = i+1
                matched_m[i+1] = propose
                break
            else:
                first = matched_w[propose]
                second = i+1
                prefer = prefer_lst[(n+propose)-1]
                if prefer.index(second) < prefer.index(first):
                    idx = prefer_lst[first-1].index(propose)
                    fail[first-1][idx] = 1
                    matched_w[propose] = second
                    matched_m[second] = propose
                    matched_m[first] = 0
                else:
                    idx = prefer_lst[second-1].index(propose)
                    fail[second-1][idx] = 1
                    matched_m[second] = 0
                break

print('(man, woman)')
print(*zip([_ for _ in range(1, n+1)], matched_m[1:]), sep = '\n')
