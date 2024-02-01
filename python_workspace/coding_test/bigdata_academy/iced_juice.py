from collections import deque

# 상하좌우
dir_r = (-1,1,0,0)
dir_c = (0,0,-1,1)


# bfs
def bfs(r,c):
    global visited
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        curr_r, curr_c = queue.pop()
        visited[curr_r][curr_c] = True

        for d in range(4):
            next_r, next_c = curr_r + dir_r[d], curr_c + dir_c[d]
            if next_r in [-1, N] or next_c in [-1, M] or visited[next_r][next_c] or tray[next_r][next_c] == '1':
                continue
            queue.appendleft((next_r, next_c))

    return 1


N, M = map(int,input().split())

visited = [[False for _ in range(M)] for _ in range(N)]
tray = [list(input()) for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and tray[i][j] == '0':
            count += bfs(i, j)

print(count)