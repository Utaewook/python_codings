# def dfs(r, c, l):
#     global path_length
#     for d in range(4):
#         curr_r = r + dr[d]
#         curr_c = c + dc[d]
#         if curr_r == n - 1 and curr_c == m - 1:
#             path_length = min(l + 1, path_length)
#             return
#
#         if curr_r in [-1, n] or curr_c in [-1, m] or maze[curr_r][curr_c] == 0:
#             continue
#         if not visited[curr_r][curr_c] and maze[curr_r][curr_c]:
#             visited[curr_r][curr_c] = True
#             dfs(curr_r, curr_c, l + 1)
#             visited[curr_r][curr_c] = False
#
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# maze = []
#
# for i in range(n):
#     row = input()
#     maze.append([])
#     for j in range(m):
#         maze[i].append(int(row[j]))
#
#
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]
#
# path_length = n * m + 1
# visited = [[False for _ in range(m)] for _ in range(m)]
#
# visited[0][0] = True
# dfs(0,0,1)
# print(path_length)

import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue.appendleft([0, 0])
    visited[0][0] = True

    while queue:
        r, c = queue.pop()
        for d in range(4):
            curr_r = r + dr[d]
            curr_c = c + dc[d]
            if curr_r == n - 1 and curr_c == m - 1:
                distance[curr_r][curr_c] = distance[r][c] + 1
                break

            if curr_r in [n, -1] or curr_c in [m, -1]:
                continue
            elif not visited[curr_r][curr_c] and maze[curr_r][curr_c]:
                visited[curr_r][curr_c] = True
                queue.append([curr_r, curr_c])
                distance[curr_r][curr_c] = distance[r][c] + 1



n, m = map(int, input().split())

maze = []

for i in range(n):
    row = input()
    maze.append([])
    for j in range(m):
        maze[i].append(int(row[j]))

distance = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]


# 상하좌우가 아니라 우하좌상 순으로 하면 최소거리 계산이 틀릴 수도 있다? ㄴㄴ 똑같음
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

bfs()

print(distance[n-1][m-1]+1)


# 정답 코드
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))  # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n - 1][m - 1]


print(bfs(0, 0))