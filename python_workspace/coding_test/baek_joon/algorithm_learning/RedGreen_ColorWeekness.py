import sys

sys.setrecursionlimit(10000) # 재귀 횟수 제한 변경
input = sys.stdin.readline

n = int(input())

grid = [[*input().strip()] for _ in range(n)]
dir_x = [-1, 1, 0, 0]
dir_y = [0, 0, -1, 1]
visited = [[False for _ in range(n)] for _ in range(n)]

color_to_chase = grid[0][0]
weakness = False


def dfs(x, y):
    for i in range(4):
        nx = x + dir_x[i]
        ny = y + dir_y[i]

        if nx >= n or nx <= -1 or ny >= n or ny <= -1:
            continue
        if weakness:
            if (not visited[nx][ny]) and grid[nx][ny] == 'B' and grid[nx][ny] == color_to_chase:
                visited[nx][ny] = True
                dfs(nx, ny)
            elif (not visited[nx][ny]) and grid[nx][ny] in ['R', 'G'] and color_to_chase in ['R', 'G']:
                visited[nx][ny] = True
                dfs(nx, ny)
        else:
            if (not visited[nx][ny]) and grid[nx][ny] == color_to_chase:
                visited[nx][ny] = True
                dfs(nx, ny)


count = [0, 0]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color_to_chase = grid[i][j]
            dfs(i, j)
            count[0] += 1

visited = [[False for _ in range(n)] for _ in range(n)]
weakness = True
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color_to_chase = grid[i][j]
            dfs(i, j)
            count[1] += 1

print(count[0], count[1])
