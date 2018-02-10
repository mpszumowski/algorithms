"""
Find the minimal perimeter of any rectangle whose area equals N.
Copyright by Codility
https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/
"""
from math import sqrt


def solution(N):
    i = int(sqrt(N))
    while i >= 1:
        if N % i == 0:
            a = i
            b = N // i
            break
        i -= 1
    return 2 * a + 2 * b
