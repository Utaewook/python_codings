# import sys
# input = sys.stdin.readline
#
#
# def is_all_house_visited(m):
#     for line in m:
#         if 1 in line:
#             return False
#     return True
#
#
# n = int(input())
# MAP = [[*map(int, input().strip())] for _ in range(n)]
# visited = [[False for _ in range(n)] for _ in range(n)]
#
# dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
# house_count = []
#
#
# start_position = (0,0)
# stack = [start_position]
# while not is_all_house_visited(MAP):
#     row, col = stack.pop()[0], stack.pop()[1]
#
#     for i in range(4):
#         row_dir = dir[i][0]
#         col_dir = dir[i][1]


# ============================= 모범 답안 =============================

import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
MAP = [[*map(int, input().strip())] for _ in range(n)]


def dfs(x, y): # dfs 재귀적으로 구현 가능
    result = 1  # 원소의 갯수 세기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <= -1 or nx >= n or ny <= -1 or ny >= n: # 다음으로 가볼 위치가 범위 밖인 경우
            continue

        if MAP[nx][ny] == 1: # 처음 방문하는 경우!
            MAP[nx][ny] = -1
            result += dfs(nx, ny)
    return result


answer = []
for i in range(n):
    for j in range(n):
        # 처음 방문하는 노드인 경우 dfs 수행한다. dfs를 시작하게 해주는 부분
        if MAP[i][j] == 1:
            MAP[i][j] = -1
            answer.append(dfs(i, j))

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])