# bubblesort

def bubblesort(n):
    cnt = 0
    for i in range(len(n) - 1):
        for j in range((len(n) - 1) - i):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
                cnt += 1
    return n

array = [3, 6, 5, 1, 2, 10, 9, 7, 4, 8]

print('Before:', array)
lst = bubblesort(array)
print('After:', array)
