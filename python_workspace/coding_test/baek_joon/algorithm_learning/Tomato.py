from collections import deque
import sys
input = sys.stdin.readline

dx = (0, 0, 1, -1, 0, 0)
dy = (1, -1, 0, 0, 0, 0)
dz = (0, 0, 0, 0, 1, -1)


def bfs(riped):
    result = 0
    temp_queue = deque(riped)
    while temp_queue:
        queue = deque()
        queue.extend(temp_queue)
        temp_queue.clear()
        result += 1

        while queue:
            curr_x, curr_y, curr_z = queue.popleft()

            for d in range(6):
                next_x = curr_x + dx[d]
                next_y = curr_y + dy[d]
                next_z = curr_z + dz[d]

                if not (0 <= next_x < H and 0 <= next_y < M and 0 <= next_z < N):
                    continue
                if not visited[next_x][next_y][next_z] and boxs[next_x][next_y][next_z] == 0:
                    temp_queue.append((next_x, next_y, next_z))
                    visited[next_x][next_y][next_z] = True
                    boxs[next_x][next_y][next_z] = 1

    return result - 1


N, M, H = map(int, input().split())
boxs = []
ripe_tomatoes = []
empty = 0
visited = [[[False for _ in range(N)] for _ in range(M)] for _ in range(H)]
day = 0

for b in range(H):
    box = []
    for r in range(M):
        row = list(map(int, input().split()))
        for c in range(N):
            if row[c] == 1:
                ripe_tomatoes.append((b, r, c))
                visited[b][r][c] = True
            elif row[c] == -1:
                empty += 1
        box.append(row)
    boxs.append(box)

if empty == N * M * H - len(ripe_tomatoes):
    day = 0
else:
    day = bfs(ripe_tomatoes)
    if 0 in sum(sum(boxs, []), []):
        day = -1

print(day)
