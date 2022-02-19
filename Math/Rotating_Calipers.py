# Rotating Calipers

def ccw(cd1, cd2, cd3):
    x1, y1 = cd1; x2, y2 = cd2; x3, y3 = cd3
    return (x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)

def cccw(cd1, cd2, cd3, cd4):
    new = [cd4[0], cd4[1]]
    new[0] -= (cd3[0]-cd2[0])
    new[1] -= (cd3[1]-cd2[1])
    return ccw(cd1, cd2, tuple(new))

def dist(cd1, cd2):
    return (cd1[0]-cd2[0])**2 + (cd1[1]-cd2[1])**2

def monotone_chain(cd):
    u = []; l = [];
    cd.sort()
    for i in cd:
        while len(l) > 1 and ccw(l[-2], l[-1], i) <= 0:
            l.pop()
        l.append(i)
    for i in reversed(cd):
        while len(u) > 1 and ccw(u[-2], u[-1], i) <= 0:
            u.pop()
        u.append(i)
    return u[:-1] + l[:-1]

def rotating_calipers(cd):     
    hull = monotone_chain(cd)
    fl1 = len(hull)
    fl2 = 1
    res1, res2 = hull[0], hull[1]
    farest = -1
    for j in range(fl1):
        while fl2+1 != j and cccw(hull[j], hull[(j+1)%fl1], hull[fl2%fl1], hull[(fl2+1)%fl1]) > 0:
            if dist(hull[j], hull[fl2%fl1]) > farest:
                res1, res2 = hull[j], hull[fl2%fl1]
                farest = dist(res1, res2)
            fl2 += 1
        if dist(hull[j], hull[fl2%fl1]) > farest:
            res1, res2 = hull[j], hull[fl2%fl1]
            farest = dist(res1, res2)
    return res1, res2

def main():
    cd = []
    n = int(input())
    for j in range(n):
        x, y = map(int, input().split())
        cd.append((x, y))
    dot1, dot2 = rotating_calipers(cd)
    print(dot1, dot2)

if __name__ == "__main__":
    main()
