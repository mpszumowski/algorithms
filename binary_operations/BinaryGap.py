"""
Longest sequence of zeros in a binary integer. Copyright by Codility
https://app.codility.com/programmers/lessons/1-iterations/
"""


def solution(N):
    N = bin(N)
    gap_max = 0
    gap = 0
    for b in N[2:]:
        if b == '0':
            gap += 1
        else:
            gap_max = max(gap_max, gap)
            gap = 0
    return gap_max
