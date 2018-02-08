"""
Find lowest positive integer missing in an array. Copyright by Codility
https://app.codility.com/programmers/lessons/4-counting_elements/
"""


def solution(A):
    N = [0] * len(A)
    for n in A:
        if 0 < n <= len(A):
            N[n - 1] += 1

    index = 1
    for n in N:
        if n == 0:
            return index
        index += 1
    return index
