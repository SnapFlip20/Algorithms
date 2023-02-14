# Merge Sort Tree

# -------------------------------------------- #
MAX = 1000
tree = [[] for _ in range(4*MAX)]
n = 10
lst = [3, 6, 1, 14, 7, 7, 12, 5, 8, 19]
"""
# initiate
for i in range(len(lst)):
    MergeSortTree.init(0, n-1, 1, i, lst[i])
for i in range(MAX*4):
    tree[i].sort()

# query(print the number of numbers greater than k between lst[from] and lst[to])
from, to, k = map(int, input().split())
print(MergeSortTree.query(0, n-1, 1, from-1, to-1, k))
"""
# -------------------------------------------- #

def upper_bound(array, n, key):
    s, e = 0, n
    while e - s:
        mid = (s+e)//2
        if array[mid] <= key:
            s = mid + 1
        else:
            e = mid
    return e
    
class MergeSortTree:
    def init(start, end, node, idx, val):
        if idx < start or idx > end:
            return
        tree[node].append(val)
        if start == end:
            return
        middle = (start+end)//2
        MergeSortTree.init(start, middle, node*2, idx, val)
        MergeSortTree.init(middle+1, end, node*2+1, idx, val)

    def query(start, end, node, left, right, val):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return len(tree[node]) - upper_bound(tree[node], len(tree[node]), val)
        middle = (start+end)//2
        return MergeSortTree.query(start, middle, node*2, left, right, val) + MergeSortTree.query(middle+1, end, node*2+1, left, right, val)
