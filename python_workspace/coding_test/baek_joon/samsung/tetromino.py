import sys
input = sys.stdin.readline

row, col = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(row)]
vector = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

result = []
visited = [[False] * col for _ in range(row)]


def dfs(r, c, answer, length):
    if length == 4:
        return paper[r][c]
    values = []
    for dir in range(4):
        next_r = r + vector[dir][0]
        next_c = c + vector[dir][1]

        if next_r >= row or next_r <= -1 or next_c >= col or next_c <= -1:
            continue
        if not visited[next_r][next_c]:
            visited[next_r][next_c] = True
            values.append(dfs(next_r, next_c, length + 1))
            return paper[next_r][next_c]+max(values)


for i in range(row):
    for j in range(col):
        visited[i][j] = True
        result.append(dfs(i, j, 0, 1))

print(max(result))
