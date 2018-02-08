"""
Find maximal product of three elements. Copyright by Codility
https://app.codility.com/programmers/lessons/4-counting_elements/
"""


def solution(A):
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-3]*A[-2]*A[-1])