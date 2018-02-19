def merge_sort(sorted_list, p, r):
    if p < r:
        q = int((r + p) / 2)
        merge_sort(sorted_list, p, q)
        merge_sort(sorted_list, q + 1, r)
        merge(sorted_list, p, q, r)


def merge(sorted_list, p, q, r):
    low_half = []
    high_half = []
    k = p
    i = 0
    j = 0

    while k <= q:
        low_half.append(sorted_list[k])
        i += 1
        k += 1

    while k <= r:
        high_half.append(sorted_list[k])
        j += 1
        k += 1

    k = p
    i = 0
    j = 0

    while i < len(low_half) and j < len(high_half):
        if low_half[i] < high_half[j]:
            sorted_list[k] = low_half[i]
            i += 1
        else:
            sorted_list[k] = high_half[j]
            j += 1
        k += 1

    while i < len(low_half):
        sorted_list[k] = low_half[i]
        i += 1
        k += 1

    while j < len(high_half):
        sorted_list[k] = high_half[j]
        j += 1
        k += 1


A = [0, 5, -2, 2, 1, -1, 4, 3]
merge_sort(A, 0, len(A) - 1)
print(A)
