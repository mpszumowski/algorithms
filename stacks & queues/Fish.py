"""
N voracious fish are moving along a river. Calculate how many fish are alive.
Copyright by Codility
https://app.codility.com/programmers/lessons/7-stacks_and_queues/
"""


def solution(A, B):
    stack = []
    live = 0
    for f in range(len(A)):
        if B[f] == 1:
            stack.append(A[f])
        else:
            while stack != []:
                if A[f] > stack[-1]:
                    stack.pop()
                else:
                    break
            if stack == []:
                live += 1
    return live + len(stack)
