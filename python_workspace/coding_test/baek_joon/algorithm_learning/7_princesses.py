seats = [list(input()) for _ in range(5)]
# visited = [[False for _ in range(5)] for _ in range(5)]

result = set()
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)  # 상하좌우 순서로 움직임

def is_valid(r, c):
    return (0 <= r < 5) and (0 <= c < 5)

def dfs(r, c, count, y_count, visited):
    if y_count > 3:
        return

    if count == 7:
        global result
        result.add(tuple(sorted(visited)))
        return

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if is_valid(nr, nc) and (nr, nc) not in visited:
            dfs(nr, nc, count+1, y_count + (seats[nr][nc] == 'Y'), visited + [(nr,nc)])

for i in range(5):
    for j in range(5):
        dfs(i,j,1, (seats[i][j] == 'Y'), [(i,j)])

print(result)
print(len(result))
