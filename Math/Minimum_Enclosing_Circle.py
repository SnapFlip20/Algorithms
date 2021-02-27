# find Minimum Enclosing Circle (in 3D)

def hyp(x, y, z):
    return x**2 + y**2 + z**2

n = int(input())

px, py, pz = 0, 0, 0
xct = []; yct = []; zct = []

for i in range(n):
    x, y, z = map(float, input().split())
    xct.append(x); yct.append(y); zct.append(z)
    px += x; py += y; pz += z

px /= ; py /= ; pz /= n

# using gradient descent
rate = 0.1
for i in range(30000):
    max_cd = 0
    radius = hyp(px - xct[0], py - yct[0], pz - zct[0])
    for j in range(1, n):
        temp = hyp(px - xct[j], py - yct[j], pz - zct[j])
        if radius < temp:
            radius = temp
            max_cd = j
    px += (xct[max_cd] - px)*rate
    py += (yct[max_cd] - py)*rate
    pz += (zct[max_cd] - pz)*rate
    rate *= 0.999

print(px, py, pz, radius**0.5)
