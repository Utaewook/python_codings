import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

queue = deque(range(1,n+1))
len_queue = n
while len_queue > 1:
    queue.popleft()
    queue.append(queue.popleft())
    len_queue -= 1

print(queue[0])