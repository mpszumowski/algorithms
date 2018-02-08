"""
Count number of passing cars. Copyright by Codility
https://app.codility.com/programmers/lessons/5-prefix_sums/
"""


def solution(A):
    east = 0
    passing = 0
    for car in A:
        if car == 0:
            east += 1
        else:
            passing += east
            if passing > 10 ** 9:
                return -1
    return passing
