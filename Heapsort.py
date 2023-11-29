from math import floor


def heap_sort(lst):
    heapify(lst)
    end = len(lst) - 1

    while end > 0:
        lst[0], lst[end] = lst[end], lst[0]
        end -= 1
        sift_down(lst, 0, end)


def heapify(lst):
    end = len(lst) - 1
    start = floor((end - 1) / 2)

    while start >= 0:
        sift_down(lst, start, end)
        start -= 1


def sift_down(lst, start, end):
    root = start

    while 2 * root + 1 < end:
        child = 2 * root + 1
        swap = root

        if lst[swap] < lst[child]:
            swap = child
        if child + 1 <= end and lst[swap] < lst[child + 1]:
            swap = child + 1
        if swap == root:
            break
        else:
            lst[root], lst[swap] = lst[swap], lst[root]
            root = swap
