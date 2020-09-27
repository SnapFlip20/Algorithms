array = [3, 6, 5, 1, 2, 10, 9, 7, 4, 8]

print('Before: ')
print(array)

for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i] #swap

print('After: ')
print(array)
