"""
Minimize the difference of two slices of an array
https://app.codility.com/programmers/lessons/3-time_complexity/
"""


def solution(A):
    left = 0
    right = 0
    min_diff = 10 ** 9 + 1
    for n in A:
        right += n
    for n in A[:-1]:
        left += n
        right -= n
        min_diff = min(min_diff, abs(left - right))
    return min_diff
