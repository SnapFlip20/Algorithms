# Slope Trick

from queue import PriorityQueue

def slope_trick(n, lst):
    res = 0
    pq = PriorityQueue()
    for i in range(n):
        lst_i = lst[i]
        lst_i -= i
        if (not pq.empty() and pq[-1] > lst_i):
            pq.put(lst_i)
            res += pq[-1] - lst_i
            pq.pop()
            pq.put(lst_i)
        else:
            pq.put(lst_i)
    return res
