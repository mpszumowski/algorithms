"""
Cover "Manhattan skyline" using the minimum number of rectangles.
Copyright by Codility
https://app.codility.com/programmers/lessons/7-stacks_and_queues/
"""


def solution(H):
    stack = []
    blcks = 0
    for b in H:
        while stack != [] and stack[-1] > b:
            stack.pop()
        if stack == []:
            stack.append(b)
            blcks += 1
        elif stack[-1] == b:
            continue
        elif stack[-1] < b:
            stack.append(b)
            blcks += 1
    return blcks
