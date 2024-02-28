# Matrix Rotation

def rotate_cw(m):
    mt = [*zip(*reversed(m))]
    return mt

def rotate_ccw(m):
    mt = [*reversed([*zip(*m)])]
    return mt

def rotate_180(m):
    mt = [reversed(i) for i in reversed(m)]
    return mt
