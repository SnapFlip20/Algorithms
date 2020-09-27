def merge(arr_left, arr_right, compare):
    arr_result = []
    i, j = 0, 0
    while i < len(arr_left) and j < len(arr_right):
        if compare(arr_left[i], arr_right[j]):
            i += 1
        else:
            arr_result.append(arr_right[j])
            j += 1
    while i < len(arr_left):
        arr_result.append(arr_left[i])
        i += 1
    while j < len(arr_right[j]):
        arr_result.append(arr_right[j])
        j += 1
    return arr_result

import operator

def mergeSort(arr, compare = operator.lt):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        left  = mergeSort(arr[:middle], compare)
        right = mergeSort(arr[middle:], compare)
        return merge(left, right, compare)
