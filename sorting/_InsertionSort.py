def insertion_sort(A):
    for i in range(1, len(A)):
        current = A[i]

        while i > 0 and A[i-1] > current:
            A[i] = A[i-1]
            i -= 1
        A[i] = current

    return A

array = [22, 11, 99, 88, 9, 7, 42]
print(insertion_sort(array))