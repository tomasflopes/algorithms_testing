import random


def insertion_sort(arr, i=1):
    if(i == len(arr)):
        return arr

    if(arr[i] > arr[i-1]):
        return insertion_sort(arr, i+1)

    j = i

    while(arr[j] < arr[j-1] and j > 0):
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1

    return insertion_sort(arr, i+1)


print('--- Best Case ---')  # O(n)
arr = []

for i in range(500):
    arr.append(i)

print(insertion_sort(arr))

print('--- Average Case ---')
arr = []

for i in range(500):
    arr.append(random.randint(1, 500))

print(insertion_sort(arr))

print('--- Worst Case ---')  # O(n^2)

arr = []
for i in range(500):
    arr.append(500-i)

print(insertion_sort(arr))
