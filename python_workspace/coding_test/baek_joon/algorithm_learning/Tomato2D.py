from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int,input().split())

storage = [list(map(int,input().split())) for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if storage[i][j] == 1:
            queue.append((i, j))

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)  # 상하좌우 순으로 탐색
day = 0

while queue:
    for _ in range(len(queue)):
        curr_r, curr_c = queue.popleft()

        for d in range(4):
            next_r, next_c = curr_r + dr[d], curr_c + dc[d]
            if (0 <= next_r < n) and (0 <= next_c < m) and (storage[next_r][next_c] == 0):
                storage[next_r][next_c] = 1
                queue.append((next_r, next_c))

    day += 1

if any(0 in row for row in storage):
    print(-1)
else:
    print(day-1)