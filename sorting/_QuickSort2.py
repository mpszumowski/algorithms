def quicksort(A):
    if len(A) <= 1:
        return A
    pivot = A[len(A) // 2]
    left = [x for x in A if x < pivot]
    middle = [x for x in A if x == pivot]
    right = [x for x in A if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([5, -1, 0, 10, 1, 2, 4, 0]))
