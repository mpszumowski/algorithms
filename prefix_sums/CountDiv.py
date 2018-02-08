"""
Compute number of integers divisible by k in range [a..b]. Copyright by Codility
https://app.codility.com/programmers/lessons/5-prefix_sums/
"""


def solution(A, B, K):
    if A % K == 0:
        return (B - A) // K + 1
    else:
        return (B - (A - A % K)) // K
