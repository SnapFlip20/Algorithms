# Divide And Conquer Optimization(D&C Opt)

def c(i, j):
    # recurrence formula here

def dncopt(s, e, l, r):
    global res
    if s > e:
        return
    m = (s+e)//2
    k = max(l, m-d)
    for i in range(k, min(r, m+d)+1):
        if (c(k, m) < c(i, m)):
            k = i
    res = max(res, c(k, m))
    dncopt(s, m-1, l, k)
    dncopt(m+1, e, k, r)
