# Find closest pair in 2d

from math import sqrt

def dist(cd1, cd2):
    return (cd1[0]-cd2[0])**2 + (cd1[1]-cd2[1])**2

def closest_pair(start, end):
    length = end - start
    if length == 0: # base case
        return 1e10
    if length == 1: # base case
        return dist(cd[start], cd[end])

    # divide
    mid = (start+end) >> 1
    min_distance = min(closest_pair(start, mid), closest_pair(mid, end))

    cd_in_range = []
    for i in range(start, end+1):
        if (cd[i][0]-cd[mid][0])**2 < min_distance:
            cd_in_range.append(cd[i])

    cd_len = len(cd_in_range)
    cd_in_range.sort(key = lambda x: x[1])
    
    for i in range(cd_len-1):
        for j in range(i+1, cd_len):
            if (cd_in_range[i][1] - cd_in_range[j][1])**2 < min_distance:
                min_distance = min(min_distance, dist(cd_in_range[i], cd_in_range[j]))
            else:
                break

    return min_distance

n = int(input())

cd = []

for i in range(n):
    cd.append(tuple(map(int, input().split())))

cd.sort()

print(sqrt(closest_pair(0, n-1)))
