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
    yield from merge_sort_recursive(0, len(elems) - 1, elems)
    yield -1, None

def merge_sort_recursive(i1, i2, elems):
    yield (0, [i1, i2])

    if i1 >= i2:
        return

    m = (i2+i1-1) // 2

    yield from merge_sort_recursive(i1, m, elems)
    yield from merge_sort_recursive(m+1, i2, elems)

    # merge sorted halfs

    sub1 = elems[i1:m+1].copy()
    sub2 = elems[m+1:i2+1].copy()

    c1 = 0
    c2 = 0
    c = i1

    while c1 < len(sub1) and c2 < len(sub2):
        if sub1[c1] <= sub2[c2]:
            elems[c] = sub1[c1]
            c1 += 1
        else:
            elems[c] = sub2[c2]
            c2 += 1
        c += 1
    
    # copy remaining 
    if c1 < len(sub1):
        elems[c:i2+1] = sub1[c1:]
    elif c2 < len(sub2):
        elems[c:i2+1] = sub2[c2:]

def quick_sort(elems):
    yield from quick_sort_recursive(elems, 0, len(elems)-1)
    yield -1, None

def quick_sort_recursive(elems, l, r):
    if l >= r:
        return
    
    p = elems[r]
    i = l

    for j in range(l, r+1):
        if elems[j] < p:
            swap(elems, i, j)
            i += 1
            
    yield(0, [i])
    # put pivot to it's position
    swap(elems, i, r)
    yield from quick_sort_recursive(elems, l, i-1)
    yield from quick_sort_recursive(elems, i+1, r)

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