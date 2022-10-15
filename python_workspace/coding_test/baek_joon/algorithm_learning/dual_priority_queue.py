import sys

input = sys.stdin.readline
from heapq import heappop, heappush, heapify


# result = []
# test_cases = int(input())
#
# for _ in range(test_cases):
#     n = int(input())
#     min_heap = []
#     max_heap = []
#     for _ in range(n):
#         op, num = input().split()
#         num = int(num)
#         if op == 'D':
#             if num == -1:
#                 if len(min_heap) == 0:
#                     continue
#                 val = heappop(min_heap)
#                 max_heap.remove((-1*val, val))
#             else:
#                 if len(max_heap) == 0:
#                     continue
#                 val = heappop(max_heap)
#                 min_heap.remove(val[1])
#
#         else:
#             heappush(min_heap, num)
#             heappush(max_heap, (num*-1, num))
#
#     max_heap = [max_heap[i][1] for i in range(len(max_heap))]
#     heap = set(min_heap).union(set(max_heap))
#     if len(min_heap) == 0 and len(max_heap) == 0:
#         result.append("EMPTY")
#     else:
#         result.append(f"{max(heap)} {min(heap)}")
#
# for r in result:
#     print(r)


################## 모범 답안 ##################


def pop(heap):
    while len(heap) > 0:
        val, idx = heappop(heap)
        if not deleted[idx]:
            deleted[idx] = True
            return val
    return None


for _ in range(int(input())):
    k = int(input())
    min_heap = []
    max_heap = []
    current = 0  # 삽입할 원소의 idx값
    deleted = [False] * (k + 1)
    for i in range(k):
        command = input().split()
        op, data = command[0], int(command[1])
        if  op == 'D':
            if data == -1: pop(min_heap)
            elif data == 1: pop(max_heap)
        elif op == 'I':
            heappush(min_heap, (data, current))
            heappush(max_heap, (-1*data, current))
            current += 1
    max_val = pop(max_heap)
    if max_val == None: print("EMPTY")
    else:
        heappush(min_heap, (-1*max_val, current))
        print(-1*max_val,pop(min_heap))