"""
Calculate the number of triplets from which a triangle can be built.
Copyright by Codility
https://app.codility.com/programmers/lessons/4-counting_elements/
"""


def solution(A):
    A.sort()
    # if A[i] + A[i+1] > A[i+2] then triplet is triangular

    for i in range(0, len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1
    return 0
