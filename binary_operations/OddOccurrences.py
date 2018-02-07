"""
Find value that occurs in odd number of instances. Copyright by Codility
https://app.codility.com/programmers/lessons/2-arrays/
"""


def solution(A):
    odd = 0
    for n in A:
        odd ^= n
    return odd
