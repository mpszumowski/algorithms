"""
Find earliest moment when the path is ready. Copyright by Codility
https://app.codility.com/programmers/lessons/4-counting_elements/
"""


def solution(X, A):
    path = [0] * X
    steps = X
    index = 0
    for n in A:
        if path[n-1] == 0:
            path[n-1] += 1
            steps -= 1
            if steps == 0:
                return index
        index += 1
    return -1