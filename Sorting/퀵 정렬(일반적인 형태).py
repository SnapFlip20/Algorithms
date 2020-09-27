# quick sort(general)

def quicksort(array, start, end):
    if start >= end: # if len(array) == 1 (escape criterion)
        return
    pivot = start # pivot = array[0]
    left = start + 1
    right = end
    while left <= right:
        # do loop(while find a number greater than pivot)
        while (left <= end) and (array[left] <= array[pivot]):
            left += 1
        # do loop(while find a number less than pivot)
        while (right > start) and (array[right] >= array[pivot]):
            right -= 1
        if left > right: # if data were crossed, swap array[pivot], array[right]
            array[right], array[pivot] = array[pivot], array[right] #swap
        else: # else, swap array[right], array[left]
            array[left], array[right] = array[right], array[left]
    quicksort(array, start, right-1)
    quicksort(array, right+1, end)

array = [3, 6, 5, 1, 2, 10, 9, 7, 4, 8]            
print('Before:', array)
print()
quicksort(array, 0, len(array) - 1)
print('After:', array)
