from collections import deque

n, k = map(int,input().split())

queue = deque(range(1, n+1))
k_queue = deque()
result = list()

count = 0
print('<', end='')
while queue:
    next_num = queue.popleft()

    k_queue.append(next_num)
    count += 1

    if count == k:
        print(k_queue.pop(), end=', ')
        count = 0

        while k_queue:
            queue.append(k_queue.popleft())



