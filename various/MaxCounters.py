"""
Calculate the values of counters. Copyright by Codility
https://app.codility.com/programmers/lessons/4-counting_elements/
"""


def solution(N, A):
    counters = [0] * N
    max_counter = 0
    last_max_counter = 0
    for op in A:
        if op > N:
            last_max_counter = max_counter
        else:
            if counters[op - 1] < last_max_counter:
                counters[op - 1] = last_max_counter
            counters[op - 1] += 1
            max_counter = max(max_counter, counters[op - 1])

    index = 0
    for counter in counters:
        if counter < last_max_counter:
            counters[index] = last_max_counter
        index += 1
    return counters
