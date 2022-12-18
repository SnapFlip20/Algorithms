# Matrix Power

def matmul(m1, m2):
    mt = []
    for i in range(len(m1)):
        mt.append([])
        for j in range(len(m2[0])):
            tmp = 0
            for k in range(len(m1[0])):
                tmp += m1[i][k]*m2[k][j]
            mt[i].append(tmp)
    return mt

def matpow(m, n):
    if n == 1:
        return m
    else:
        div = matpow(m, n//2)
        if n % 2 == 0:
            return matmul(div, div)
        else:
            return matmul(matmul(div, div), m)
