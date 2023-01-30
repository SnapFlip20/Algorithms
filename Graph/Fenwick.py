# Fenwick Tree

# -------------------------------------------- #
n = 10
tree = [0 for _ in range(n+1)]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
# initiate
for i in range(1, n+1):
    FenwickTree.update(i, lst[i])
"""
# -------------------------------------------- #

class FenwickTree:
    def update(i, dif):
        while i < len(tree):
            tree[i] += dif
            i += (i & -i)
    
    def query_sum(i):
        res = 0
        while i > 0:
            res += tree[i]
            i -= (i & -i)
        return res
