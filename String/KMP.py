# KMP

def kmp(text, pattern):
    n, m = len(text), len(pattern)
    fail = [0 for _ in range(m+1)]

    j = 0
    for i in range(1, m):
        while (j > 0 and pattern[i] != pattern[j]):
            j = fail[j-1]
        if (pattern[i] == pattern[j]):
            j += 1
            fail[i] = j

    res = []
    j = 0
    for i in range(n):
        while (j > 0 and text[i] != pattern[j]):
            j = fail[j-1]
        if (text[i] == pattern[j]):
            if (j == m-1):
                res.append(i-m+2)
                j = fail[j]
            else:
                j += 1

    return res
