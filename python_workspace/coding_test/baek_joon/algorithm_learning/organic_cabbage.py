from collections import deque

def is_valid(r, c):
    return (0 <= r < n) and (0 <= c < m)

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

for _ in range(int(input())):
    m, n, k = map(int,input().split())
    coords = list()
    visited = dict()

    for _ in range(k):
        coord = tuple(map(int,input().split()))
        coords.append(coord)
        visited[coord] = False

    count = 0
    for i in range(n):
        for j in range(m):
            if ((i, j) in coords) and not visited[(i,j)]:
                queue = deque()
                queue.append((i,j))

                while queue:
                    r, c = queue.popleft()
                    visited[(r, c)] = True

                    for d in range(4):
                        nr, nc = r+dr[d], c+dc[d]
                        if is_valid(nr, nc) and (nr,nc) in coords and not visited[(nr,nc)]:
                            queue.append((nr, nc))

                count += 1
    print(count)