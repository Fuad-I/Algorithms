from collections import Counter
from math import log, floor


def radix_sort(lst):
    k = max(lst)
    for i in range(1, floor(log(k, 10)+1)+1):
        lst = counting_sort(lst, i)
    return lst


def counting_sort(lst, digit=None):
    k = max(lst) + 1
    output = list()
    empty = [[] for _ in range(k)]

    if digit:
        for item in lst:
            empty[get_digit(item, digit)].append(item)
    else:
        for item in lst:
            empty[item].append(item)

    for i in range(k):
        output.extend(empty[i])

    return output


def get_digit(num, p):
    return num % 10**p // 10**(p-1)


def counting_sort2(lst):
    count = Counter(lst)
    output = list()
    for i in range(max(lst)+1):
        if count.get(i):
            output.extend(count.get(i)*[i])
    return output
