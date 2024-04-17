from collections import deque

n, k = map(int,input().split())

queue = deque(range(1, n + 1))
k_queue = deque()

while queue:

    while len(k_queue) < k:
        k_queue.append(queue.popleft())
