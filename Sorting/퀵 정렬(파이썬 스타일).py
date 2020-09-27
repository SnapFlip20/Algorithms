# quick sort(python style)

def quicksort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:] # list except pivot

    left = [x for x in tail if x <= pivot] # left part
    right = [x for x in tail if x > pivot] # right part
    
    # after segmentation, sort left/right parts and return the entire array
    return quicksort(left) + [pivot] + quicksort(right)

array = [3, 6, 5, 1, 2, 10, 9, 7, 4, 8]            
print('Before:', array)
print()
print('After:', quicksort(array))
