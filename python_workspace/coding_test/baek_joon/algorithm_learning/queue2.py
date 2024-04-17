import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
for _ in range(int(input())):
    line = input().rstrip()

    if 'push' in line:
        queue.append(int(line.split()[1]))
    elif line == 'front':
        print(queue[0] if queue else -1)
    elif line == 'back':
        print(queue[-1] if queue else -1)
    elif line == 'pop':
        if queue:
            d = queue.popleft()
            print(d)
        else:
            print(-1)
    elif line == 'size':
        print(len(queue))
    else:
        print(0 if queue else 1)
