def swap(elem, i, j):
    temp = elem[j]
    elem[j] = elem[i]
    elem[i] = temp

def selection_sort(elems):
    for i in range(0, len(elems) - 1):
        idx = i
        value = elems[i]
        for j in range(i+1, len(elems)):
            if(elems[j] < value):
                value = elems[j]
                idx = j
        swap(elems, idx, i)
        yield (i, [idx, i])
    yield (-1, None)

def bubble_sort(elems):
    n = len(elems)
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, n - 1):
            if elems[i+1] < elems[i]:
                swap(elems, i+1, i)
                swapped = True
                yield 0, [i, i+1]
    yield -1, None

def insertion_sort(elems):
    for i in range(1, len(elems)):
        s = i
        while(elems[s] < elems[s-1] and (s-1) >= 0):
            swap(elems, s, s-1)
            s -= 1
            yield 0, [s, s-1]
    yield -1, None

def merge_sort(elems):
    raise NotImplementedError

def quick_sort(elems):
    raise NotImplementedError

def heap_sort(elems):
    raise NotImplementedError

def counting_sort(elems):
    b = max(elems)
    n = len(elems)
    # make n counts
    count = [0] * (b + 1)

    # calculate counts
    for elem in elems:
        count[elem] += 1

    # calculate sum of previous counts
    for i in range(1, b):
        count[i+1] += count[i]

    elems_c = elems.copy()
    
    for i in range(0, n):
        e = elems_c[i]
        elems[count[e] - 1] = e
        count[e] -= 1
        yield (0, [i])

    yield (-1, None)

def radix_sort(elems):
    raise NotImplementedError

ALGORITHMS = {
                'selection_sort': selection_sort,
                'bubble_sort': bubble_sort,
                'insertion_sort': insertion_sort,
                'merge_sort': merge_sort,
                'quick_sort': quick_sort,
                'heap_sort': heap_sort,
                'counting_sort': counting_sort,
                'radix_sort': radix_sort,
            }