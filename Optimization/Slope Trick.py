# Slope Trick

'''
n = 7
a_i = 9 4 8 20 14 15 18 (input example)

b_i = 6 7 8 13 14 15 18 (output example)
'''

from heapq import heappush, heappushpop

def slope_trick(n, lst):
    pq = []; seq = []
    res = 0
    
    for (i, j) in enumerate(ai):
        a = j-i
        heappush(pq, -a)
        top = -pq[0]
        if pq and top > a:
            res += top - a
            heappushpop(pq, -a)
        seq.append(top)
    
    for i in range(n-2, -1, -1):
        if seq[i] > seq[i+1]:
            seq[i] = seq[i+1]

    for (i, j) in enumerate(seq):
        print(i + j)



n = int(input())
ai = map(int, input().split())

slope_trick(n, ai)
