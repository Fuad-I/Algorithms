def merge(array, left, right):
    while left and right:
        if left[0] <= right[0]:
            array.append(left.pop(0))
        else:
            array.append(right.pop(0))

    if right:
        array.extend(right)
    elif left:
        array.extend(left)


def merge2(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    i = start
    while left and right:
        if left[0] <= right[0]:
            array[i] = left.pop(0)
        else:
            array[i] = right.pop(0)
        i += 1

    if right:
        array[i:end] = right
    elif left:
        array[i:end] = left


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = [array.pop(0) for _ in range(mid)]
        right = [array.pop(0) for _ in range(len(array))]
        merge_sort(left)
        merge_sort(right)
        merge(array, left, right)
