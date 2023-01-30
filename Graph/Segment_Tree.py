# Segment Tree

# -------------------------------------------- #
n = 10
mod = 10**9+7
tree = [0 for _ in range(4*n)]
lazy = [0 for _ in range(4*n)]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#SegTree.init(0, n-1, 1)
# -------------------------------------------- #

# 구간합
class SegTree:
    def init(start, end, node):
        if start == end:
            tree[node] = lst[start]
            return tree[node]
        middle = (start+end)//2
        tree[node] = SegTree.init(start, middle, node*2)+SegTree.init(middle+1, end, node*2+1)
        return tree[node]
    
    def update(start, end, node, idx, dif):
        if idx < start or idx > end:
            return
        tree[node] += dif
        if start == end:
            return
        middle = (start+end)//2
        SegTree.update(start, middle, node*2, idx, dif)
        SegTree.update(middle+1, end, node*2+1, idx, dif)
        
    def query(start, end, node, left, right):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return tree[node]
        middle = (start+end)//2
        return SegTree.query(start, middle, node*2, left, right)+SegTree.query(middle+1, end, node*2+1, left, right)

# 느리게 갱신되는 구간합
class SegTree:
    def init(start, end, node):
        if start == end:
            tree[node] = lst[start]
            return tree[node]
        middle = (start+end)//2
        tree[node] = SegTree.init(start, middle, node*2) + SegTree.init(middle+1, end, node*2+1)
        return tree[node]

    def update_lazy(start, end, node):
        if lazy[node] != 0:
            tree[node] += (end-start+1)*lazy[node]
            if start != end:
                lazy[node*2] += lazy[node]
                lazy[node*2+1] += lazy[node]
            lazy[node] = 0
    
    def update_range(start, end, node, left, right, dif):
        SegTree.update_lazy(start, end, node)
        if left > end or right < start:
            return
        if left <= start and end <= right:
            tree[node] += (end-start+1)*dif
            if start != end:
                lazy[node*2] += dif
                lazy[node*2+1] += dif
            return
        middle = (start+end)//2
        SegTree.update_range(start, middle, node*2, left, right, dif)
        SegTree.update_range(middle+1, end, node*2+1, left, right, dif)
        tree[node] = tree[node*2] + tree[node*2+1]
        
    def query(start, end, node, left, right):
        SegTree.update_lazy(start, end, node)
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return tree[node]
        middle = (start+end)//2
        return SegTree.query(start, middle, node*2, left, right) + SegTree.query(middle+1, end, node*2+1, left, right)

# 구간곱
class SegTree:
    def init(start, end, node):
        if start == end:
            tree[node] = lst[start]
            return tree[node]
        middle = (start+end)//2
        tree[node] = (SegTree.init(start, middle, node*2)%mod)*(SegTree.init(middle+1, end, node*2+1))%mod
        return tree[node]
    
    def update(start, end, node, idx, dif):
        if idx < start or idx > end:
            return
        if start == end:
            tree[node] = dif
            return
        middle = (start+end)//2
        SegTree.update(start, middle, node*2, idx, dif)
        SegTree.update(middle+1, end, node*2+1, idx, dif)
        tree[node] = (tree[node*2]*tree[node*2+1])%mod
        
    def query(start, end, node, left, right):
        if left > end or right < start:
            return 1
        if left <= start and end <= right:
            return tree[node]
        middle = (start+end)//2
        return (SegTree.query(start, middle, node*2, left, right)*SegTree.query(middle+1, end, node*2+1, left, right))%mod

# 구간최솟값
class SegTree:
    def init(start, end, node):
        if start == end:
            tree[node] = lst[start]
            return tree[node]
        middle = (start+end)//2
        tree[node] = min(SegTree.init(start, middle, node*2), SegTree.init(middle+1, end, node*2+1))
        return tree[node]

    def update(start, end, node, idx, value):
        if idx < start or idx > end:
            return
        if start == end:
            tree[node] = value
            return
        middle = (start+end)//2
        SegTree.update(start, middle, node*2, idx, value)
        SegTree.update(middle+1, end, node*2+1, idx, value)
        tree[node] = min(tree[node*2], tree[node*2+1])
        
    def query(start, end, node, left, right):
        if left > end or right < start:
            return float('inf')
        if left <= start and end <= right:
            return tree[node]
        middle = (start+end)//2
        return min(SegTree.query(start, middle, node*2, left, right), SegTree.query(middle+1, end, node*2+1, left, right))

# 구간최댓값
class SegTree:
    def init(start, end, node):
        if start == end:
            tree[node] = lst[start]
            return tree[node]
        middle = (start+end)//2
        tree[node] = max(SegTree.init(start, middle, node*2), SegTree.init(middle+1, end, node*2+1))
        return tree[node]

    def update(start, end, node, idx, value):
        if idx < start or idx > end:
            return
        if start == end:
            tree[node] = value
            return
        middle = (start+end)//2
        SegTree.update(start, middle, node*2, idx, value)
        SegTree.update(middle+1, end, node*2+1, idx, value)
        tree[node] = max(tree[node*2], tree[node*2+1])
        
    def query(start, end, node, left, right):
        if left > end or right < start:
            return float('-inf')
        if left <= start and end <= right:
            return tree[node]
        middle = (start+end)//2
        return max(SegTree.query(start, middle, node*2, left, right), SegTree.query(middle+1, end, node*2+1, left, right))
