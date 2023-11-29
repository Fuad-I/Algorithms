from math import floor


def comb_sort(array, shrink):
    gap = floor(len(array) / shrink)
    while True:
        swapped = False
        for i in range(0, len(array) - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
        print(gap, array)
        gap = floor(gap / shrink)

        if not swapped and gap == 0:
            break
