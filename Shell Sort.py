def shell_sort(array, gaps):
    for gap in gaps:
        for k in range(gap):
            j = gap + k
            while j < len(array):
                i = j
                while i >= gap:
                    if array[i] < array[i - gap]:
                        array[i], array[i - gap] = array[i - gap], array[i]
                        i -= gap
                    else:
                        break
                j += gap


# same code, inner loops abstracted into a function
def shell_sort2(array, gaps):
    for gap in gaps:
        for i in range(gap):
            gap_sort(array, gap, i)


def gap_sort(array, gap, place):
    j = gap + place
    while j < len(array):
        i = j
        while i >= gap:
            if array[i] < array[i - gap]:
                array[i], array[i - gap] = array[i - gap], array[i]
                i -= gap
            else:
                break
        j += gap
