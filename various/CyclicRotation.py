"""
Rotate an array to the right by a given number of steps. Copyright by Codility
https://app.codility.com/programmers/lessons/2-arrays/
"""


def solution(A, K):
    if A == []:
        return []
    r_num = K % len(A)
    return A[-r_num:] + A[:-r_num]
