# Upper Bound

def upper_bound(array, n, key):
    s, e = 0, n
    while e - s:
        mid = (s+e)//2
        if array[mid] <= key:
            s = mid + 1
        else:
            e = mid
    return e
