"""
Find missing element in array from 1 to N. Copyright by Codility
https://app.codility.com/programmers/lessons/3-time_complexity/
"""


def solution(A):
    N = len(A) + 1
    A_sum = sum(A)
    n_sum = N * (N + 1) // 2
    return n_sum - A_sum
