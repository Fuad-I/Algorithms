from math import floor as floor
from math import ceil as ceil


def selection_sort(array, start=0, end=None):
    if not end:
        end = len(array)

    for i in range(start, end):
        min_idx = i
        for j in range(i, end):
            if array[j] < array[min_idx]:
                min_idx = j
        if not i == min_idx:
            array[i], array[min_idx] = array[min_idx], array[i]


def selection_sort_recursive(array, start=0, end=None):
    if not end:
        end = len(array)

    min_idx = start
    for i in range(start+1, end):
        if array[i] < array[min_idx]:
            min_idx = i
    array[start], array[min_idx] = array[min_idx], array[start]
    if start < end-1:
        selection_sort_recursive(array, start+1, end)


def bubble_sort(array):
    n = len(array)
    while True:
        swapped = False
        for i in range(n-1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if not swapped:
            break

        n -= 1


def bucket_sort(array):
    m = max(array) + 1
    bucket_num = ceil(m/10)
    buckets = [[] for _ in range(bucket_num)]
    for _ in range(len(array)):
        buckets[floor(bucket_num * array[0] / m)].append(array.pop(0))
    for item in buckets:
        array.extend(sorted(item))


def insertion_sort(array, start=0, end=None):
    if end is None:
        end = len(array)

    if end < start:
        raise ValueError('end must be smaller than start')

    for i in range(1, end):
        j = i
        while j > start and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


temp = [int(x) for x in '457868543']
temp2 = [int(x) for x in '457868543']
selection_sort(temp)
bubble_sort(temp2)
print(temp == temp2)
temp3 = [43, 12, 5, 24, 29, 3, 17, 9, 31, 47, 37]
bucket_sort(temp3)
print(temp3)
