# Lomuto partition scheme
def partition(arr, low, high):
    i = low
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


# Hoare partition scheme
def partition2(array, low, high):
    pivot = array[(high + low) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            return j


# Hoare partition scheme
def partition3(array, low, high):
    pivot = array[(high + low) // 2]
    i = low
    j = high
    while i < j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    return j


def quick_sort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)


def quick_sort2(array, low, high):
    if low < high:
        p = partition2(array, low, high)
        quick_sort2(array, low, p)
        quick_sort2(array, p + 1, high)


def quick_sort3(array, low, high):
    if low < high:
        p = partition3(array, low, high)
        quick_sort3(array, low, p)
        quick_sort3(array, p + 1, high)


temp = [int(x) for x in '3541737665443589054321']
quick_sort3(temp, 0, len(temp)-1)
print(temp)
