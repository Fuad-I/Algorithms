from MergeSort import merge

BLOCK = 32


def timsort(array):
    for i in range(0, len(array), BLOCK):
        insertion_sort(array, i, min(i + BLOCK, len(array) - 1))
    for i in range(0, len(array), 2*BLOCK):
        merge(array, i, i+BLOCK)