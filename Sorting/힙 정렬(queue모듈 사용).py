# using heap sort

import numpy as np
import os, queue, random, sys, time

def genRandList(size): # generate random list
    A = list(range(size)) 
    return A

def heapSort(A): # 힙 정렬
    pq = queue.PriorityQueue(maxsize = 0) # using queue module
    for i in A:
        pq.put((i, i))
    sorted_A = [] # save result
    for j in range(len(A)):
        ent = pq.get() # i: (priority, key)
        sorted_A.append(ent[1])        
    return sorted_A

def main():
    L = genRandList(20) # generate random list
    random.shuffle(L) # shuffle
    print('Before: ')
    print(L)
    print()
    t1 = time.time() # before time
    sorted_L = heapSort(L) # heap sort
    t2 = time.time() # after time
    print('After: ')
    print(sorted_L) # print list
    print()
    print('소요시간:', t2 - t1)

if __name__ == "__main__":
    main()
