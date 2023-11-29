def jump_search(array, target):
    if len(array) == 0:
        return -1
    jump = int(len(array) ** 0.5)
    i = 0
    while i < len(array):
        if array[i] == target:
            return i
        elif array[i] > target and i > 0:
            for j in range(1, jump):
                if array[i-j] == target:
                    return i-j

        i += jump
    
    # check the targets at the end that were skipped
    for k in range(jump-1):
        if array[len(array) - k - 1] == target:
            return len(array) - k - 1
    return -1


def binary_search(array, target, left=None, right=None):
    if not array:
        print('Empty Array')
        return -1
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    while left <= right:
        mid = (left + right)//2
        if target < array[mid]:
            right = mid - 1
        elif target > array[mid]:
            left = mid + 1
        else:
            return mid
    return -1


def rbinary_search(array, target, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if right > left:
        mid = left + (right - left) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            return rbinary_search(array, target, left, mid - 1)

        else:
            return rbinary_search(array, target, mid + 1, right)

    else:
        return -1


arr2 = [int(x) for x in '123456789']
for item in arr2:
    print(binary_search(arr2, item, 3))
    # print(binary_search(arr, item))

