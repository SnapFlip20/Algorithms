# quick sort
def quicksort(n):
    if len(n) > 1:
        a = n[0]
        (c, d) = partitionfunc(a, n[1:])
        return quicksort(c) + [a] + quicksort(d)
    else:
        return n

def partitionfunc(a, n):
    c, d = [], []
    for i in n:
        if i < a:
            c.append(i)
        else:
            d.append(i)
    return c, d

array = [3, 6, 5, 1, 2, 10, 9, 7, 4, 8]

print('Before:', array)
print()
print('After:', quicksort(array))
