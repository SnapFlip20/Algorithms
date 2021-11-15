# Find closest pair in 2d

def return_dist(cd1, cd2):
    return (cd1[0] - cd2[0])**2 + (cd1[1] - cd2[1])**2

def closest_pair(cd, n):
    if n == 2:
        return return_dist(cd[0], cd[1])
    elif n == 3:
        return min(return_dist(cd[0], cd[1]), return_dist(cd[1], cd[2]), return_dist(cd[0], cd[2]))
    distance = min(closest_pair(cd[(n//2):], n//2), closest_pair(cd[:(n//2)], n//2))

    middle = (cd[n//2][0]+cd[n//2-1][0]) // 2
    cd_in_range = [] 
    for i in cd:
        if (middle-i[0])**2 <= distance:
            cd_in_range.append(i)

    cd_in_range = sorted(cd_in_range, key = lambda x: x[1])

    if len(cd_in_range) == 1:
        return distance
    else:
        min_distance = distance
        for i in range(len(cd_in_range)-1):
            for j in range(i+1, len(cd_in_range)):
                if (cd_in_range[i][1]-cd_in_range[j][1])**2 > distance:
                    break
                elif cd_in_range[i][0] < middle and cd_in_range[j][0] < middle:
                    continue
                elif cd_in_range[i][0] > middle and cd_in_range[j][0] > middle:
                    continue
                min_distance = min(min_distance, return_dist(cd_in_range[i], cd_in_range[j]))
    return min_distance

n = int(input())

coordinate = []

for i in range(n):
    coordinate.append(tuple(map(int, input().split())))

coordinate = list(set(map(tuple, coordinate)))

if len(coordinate) != n:
    print(0)
else:
    coordinate.sort()
    print(closest_pair(coordinate, n))
