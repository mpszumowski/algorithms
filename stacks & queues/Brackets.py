"""
Determine whether a given string of parentheses is properly nested.
Copyright by Codility
https://app.codility.com/programmers/lessons/7-stacks_and_queues/
"""


def solution(S):
    stack = []
    for b in S:
        if stack == []:
            stack.append(b)
        else:
            if stack[-1] == "(" and b == ")":
                stack.pop()
            elif stack[-1] == "[" and b == "]":
                stack.pop()
            elif stack[-1] == "{" and b == "}":
                stack.pop()
            else:
                stack.append(b)
    if stack == []:
        return 1
    return 0