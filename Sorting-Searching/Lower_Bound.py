# Lower Bound

array = []

def lower_bound(n, key):
    s, e = 0, n-1
    while s < e:
        mid = (s+e)//2
        if array[mid] < key:
            s = mid+1
        else:
            e = mid
    return e
