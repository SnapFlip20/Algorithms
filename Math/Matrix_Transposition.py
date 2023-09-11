# Matrix Transposition

def matts(m):
    row = len(m)
    col = len(m[0])
    mt = [[0 for _ in range(row)] for _ in range(col)]

    for i in range(row):
        for j in range(col):
            mt[j][i] = m[i][j]
    
    return mt
