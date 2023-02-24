# Matrix Addition

def matadd(m1, m2):
    mt = []
    row = len(m1)
    col = len(m1[0])
    for i in range(row):
        mt.append([])
        for j in range(col):
            mt[i].append(m1[i][j] + m2[i][j])
    return mt