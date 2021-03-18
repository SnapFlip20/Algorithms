# find convex hull

def ccw(cd1, cd2, cd3):
    x1, y1 = cd1; x2, y2 = cd2; x3, y3 = cd3
    return (x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)

def slope(cd1, cd2):
    if cd1[0] != cd2[0]:
        return 1.0*(cd1[1]-cd2[1])/(cd1[0]-cd2[0])
    else:
        return float('inf')

def dist(cd1, cd2):
    return ((cd1[0]-cd2[0])**2 + (cd1[1]-cd2[1])**2)**0.5

n = int(input())
cd = []

for i in range(n):
    x, y = map(int, input().split())
    cd.append((x, y))

start = min(cd, key = lambda x: (x[0], x[1]))

cd.pop(cd.index(start))

sorted_cd = sorted(cd, key = lambda x: (slope(x, start), dist(x, start)))

st = [start, sorted_cd[0]]

for i in range(1, n-1):
    while len(st) > 1 and ccw(st[-2], st[-1], sorted_cd[i]) <= 0:
        st.pop()
    st.append(sorted_cd[i])

print(len(st))
print(st)
