from heapq import *


def solution(k, tangerine):
    answer = 0
    count = [0 for _ in range(max(tangerine)+1)]
    for t in tangerine:
        count[t] += 1
    count = [(count[i],i) for i in range(len(count))]
    heapify(count)
    while k > 0:
        c = heappop(count)
        k -= c
        answer += 1
    return answer