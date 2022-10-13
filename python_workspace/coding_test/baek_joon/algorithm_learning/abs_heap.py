import sys
input = sys.stdin.readline
from heapq import heappop, heappush

que = []
result = list()

n = int(input())
for _ in range(n):
    val = int(input())
    if val == 0:
        if len(que) == 0:
            result.append(0)
        else:
            result.append(heappop(que)[1])
    else:
        heappush(que,(abs(val), val))

for n in result:
    print(n)