"""
Calculate the number of distinct values in an array. Copyright by Codility
https://app.codility.com/programmers/lessons/4-counting_elements/
"""


def solution(A):
    if A == []:
        return 0
    A.sort()
    distinct_vals = 1
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            distinct_vals += 1
    return distinct_vals
