# python3으로 컴파일시 시간초과로 실패함 - pypy3으로 컴파일 하여 성공
# 하드코딩을 통해 코딩 해볼것
# 500*500의 데이터 입력의 경우에 램 8기가 / cpu = ryzen5 4000 series 의 경우에 약 10초 정도 소요됨

import sys

input = sys.stdin.readline

row, col = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(row)]
vector = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

max_val = -1
visited = [[False] * col for _ in range(row)]
not_dfs_shape = [[(0, -1), (0, 0), (0, 1), (1, 0)],  # ㅜ
                 [(0, -1), (0, 0), (0, 1), (-1, 0)],  # ㅗ
                 [(0, -1), (0, 0), (-1, 0), (1, 0)],  # ㅓ
                 [(0, 1), (0, 0), (-1, 0), (1, 0)]]  # ㅏ


def dfs(r, c, length, sums):
    global max_val

    if length == 4:
        max_val = max(max_val, sums + paper[r][c])
        return
    for i in range(4):
        nr = r + vector[i][0]
        nc = c + vector[i][1]

        if nr >= row or nr <= -1 or nc >= col or nc <= -1:
            continue
        if not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, length + 1, sums + paper[r][c])
            visited[nr][nc] = False
    return


def not_dfs(i, j):
    global max_val
    for shape in not_dfs_shape:
        i0 = i + shape[0][0]; j0 = j + shape[0][1]
        i1 = i + shape[1][0]; j1 = j + shape[1][1]
        i2 = i + shape[2][0]; j2 = j + shape[2][1]
        i3 = i + shape[3][0]; j3 = j + shape[3][1]
        if -1 in [i0,j0,i1,j1,i2,j2,i3,j3] or row in [i0,i1,i2,i3] or col in [j0,j1,j2,j3]:
            continue
        max_val = max(max_val, paper[i0][j0]+paper[i1][j1]+paper[i2][j2]+paper[i3][j3])


for i in range(row):
    for j in range(col):
        visited[i][j] = True
        dfs(i, j, 1, 0)
        visited[i][j] = False
        not_dfs(i, j)

print(max_val)
