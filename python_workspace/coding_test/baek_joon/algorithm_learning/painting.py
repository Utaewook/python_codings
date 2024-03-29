from collections import deque


n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)  # 하, 상, 우, 좌 순서

paints = list()

def bfs(start_r, start_c):
    global max_size
    queue = deque()
    queue.append((start_r,start_c))
    count = 0

    while queue:
        r, c = queue.popleft()
        if visited[r][c]:
            continue

        visited[r][c] = True
        count += 1
        for d in range(4):
            next_r, next_c = r + dr[d], c + dc[d]
            if next_r in [-1, n] or next_c in [-1, m]:
                continue

            if paper[next_r][next_c] == 1 and not visited[next_r][next_c]:
                queue.append((next_r, next_c))
    paints.append(count)




for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

if paints:
    print(len(paints))
    print(max(paints))
else:
    print(0)
    print(0)