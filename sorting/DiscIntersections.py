"""
Compute the number of disc intersections. Copyright by Codility
https://app.codility.com/programmers/lessons/4-counting_elements/
"""


def solution(A):
    # an intersections occurs iff:
    # A[J] + J >= A[K] - K
    # and
    # A[J] - J <= A[K] + K
    # (this includes cases where J=K)
    # for any A[J] + J if K meets the first condition,
    # then K meets the first condition for A[J+n] + J+n
    J = []
    K = []
    index = 0
    for disc in A:
        J.append(index + disc)
        K.append(index - disc)
        index += 1

    J.sort()
    K.sort()

    intersection = 0
    i = 0
    for d in range(0, len(J)):
        intersection += i
        while i < len(K) and J[d] >= K[i]:
            intersection += 1
            i += 1

    intersection -= len(J) * (len(J) + 1) // 2
    if intersection > 10 ** 7:
        return -1

    return intersection
