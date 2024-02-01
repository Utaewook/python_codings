from collections import deque


def bfs(r, c, h):
    if board[r][c] <= h or visited[r][c]:
        return

    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    safety_area = set()

    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)

    while queue:
        curr_r, curr_c = queue.popleft()
        safety_area.add((curr_r, curr_c))

        for i in range(4):
            next_r, next_c = curr_r + dr[i], curr_c + dc[i]
            if next_r >= n or next_r < 0 or next_c >= n or next_c < 0:
                continue

            if board[next_r][next_c] > h and not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                queue.append((next_r, next_c))
    return tuple(safety_area)


n = int(input())

board = []
safety_zone = 1

for _ in range(n):
    board.append(list(map(int, input().split())))


for height in range(1,101):
    safety = set()
    visited = [[False for _ in range(n)] for _ in range(n)]

    for row in range(n):
        for col in range(n):
            result = bfs(row,col,height)
            if result:
                safety.add(result)

    safety_zone = max(safety_zone, len(safety))


print(safety_zone)