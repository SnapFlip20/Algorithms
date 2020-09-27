# insertionsort

def insertionsort(n):
    for i in range(1, len(n)):
        j = i - 1
        num = n[i]
        while n[j] > num and j >= 0:
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = num
    return n

array = [3, 6, 5, 1, 2, 10, 9, 7, 4, 8]

print('Before:', array)
print()
print('After:', insertionsort(array))

