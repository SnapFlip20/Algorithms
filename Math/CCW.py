# CCW(Counter ClockWise)

'''
세 점 a, b, c가 반시계 방향일 경우 1
시계 방향일 경우 -1
일직선이면 0
'''

def ccw(cd1, cd2, cd3):
    x1, y1 = cd1; x2, y2 = cd2; x3, y3 = cd3
    res = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0
