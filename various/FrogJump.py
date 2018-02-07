"""
Count minimal number of jumps. Copyright by Codility
https://app.codility.com/programmers/lessons/3-time_complexity/
"""


def solution(X, Y, D):
    return int((Y - X) / D) + int((Y - X) % D > 0)
