import sys

input = sys.stdin.readline

import time

# dfs 시간초과 나면 bfs로 풀이할걸 (앵간하면 bfs로 풀어보자)
def dfs(row, col):
    global path, result

    for d in range(4):
        next_row = row + dr[d]
        next_col = col + dc[d]
        if next_row >= R or next_row < 0 or next_col >= C or next_col < 0 or board[next_row][next_col] in path or \
                visited[next_row][next_col]:
            continue
        else:
            visited[next_row][next_col] = True
            path.add(board[next_row][next_col])
            dfs(next_row, next_col)
            result = max(result, len(path))
            visited[next_row][next_col] = False
            path.remove(board[next_row][next_col])


def bfs(row, col):
    global result

    q = set()
    q.add((row, col, board[row][col]))
    while q:
        r, c, step = q.pop()
        result = max(result, len(step))

        for d in range(4):
            next_row = r + dr[d]
            next_col = c + dc[d]
            if 0 <= next_row < R and 0 <= next_col < C and board[next_row][next_col] not in step:
                q.add((next_row, next_col, step+board[next_row][next_col]))


R, C = map(int, input().split())
visited = [[False for _ in range(C)] for _ in range(R)]
dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)
board = []
path = set()
result = 0

for _ in range(R):
    board.append(list(input()))

result = 0
start = time.time()
bfs(0, 0)
print(f"bfs result = {result}  / takes {time.time() - start}")

visited[0][0] = True
path.add(board[0][0])
start = time.time()
dfs(0, 0)
print(f"dfs result = {result}  / takes {time.time() - start}")

print(result)
