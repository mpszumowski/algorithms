def swap(qlist, first_index, second_index):
    qlist[first_index], qlist[second_index] = qlist[second_index], qlist[first_index]


def partition(qlist, lo, hi):
    pivot_position = next_to_compare = lo
    while next_to_compare < hi:
        if qlist[next_to_compare] <= qlist[hi]:
            swap(qlist, next_to_compare, pivot_position)
            next_to_compare += 1
            pivot_position += 1
        else:
            next_to_compare += 1
    swap(qlist, hi, pivot_position)
    return pivot_position


def quick_sort(qlist, lo, hi):
    if lo < hi:
        pivot = partition(qlist, lo, hi)
        quick_sort(qlist, lo, pivot - 1)
        quick_sort(qlist, pivot + 1, hi)


a = [3, 0, -1, -2, 2, 1]
quick_sort(a, 0, len(a) - 1)
print(a)