# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop
#
# heap = []
# result = []
# k, n = map(int, input().split())
# pn = list(map(int,input().split()))
#
# for num in pn:
#     heappush(heap, num)
#
# while len(heap) < n:
#     val = heap[0]
#     temp = [val*a for a in pn]
#     result.append(heappop(heap))
#     for m in temp:
#         if m not in heap:
#             heappush(heap, m)
#
#
# print(heap)
# print(max(heap))


import sys
input = sys.stdin.readline
import heapq

k, n = map(int,input().split())
data = list(map(int,input().split()))

heap = []
visited = set()
max_value = max(data)

for x in data:
    heapq.heappush(heap, x)

for i in range(n-1):
    element = heapq.heappop(heap)
    for x in data:
        now = element * x
        if len(heap) >= n and max_value < now:
            continue
        if now not in visited:
            heapq.heappush(heap,now)
            max_value = max(max_value,now)
            visited.add(now)

print(heapq.heappop(heap))
print(heap)