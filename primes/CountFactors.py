"""
Count factors of given number n. Copyright by Codility
https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/
"""
from math import sqrt


def solution(N):
    factors = 0
    i = 1
    while i < sqrt(N):
        if N % i == 0:
            factors += 2
        i += 1
    if i * i == N:
        factors += 1
    return factors
