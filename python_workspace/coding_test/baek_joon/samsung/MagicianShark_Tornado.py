def move(r, c):
    r_temp, c_temp = r, c
    grid_visit[r][c] = True
    grid[r][c] = SUM
    up, down, left, right = grid_visit[r-1][c], grid_visit[r+1][c], grid_visit[r][c-1], grid_visit[r][c+1]
    if (up and right) or ((not up) and (not down) and right):  # 밑으로 가야 하는 경우
        r_temp -= 1
    elif (up and left) or ((not left) and (not right) and up):  # 오른 쪽으로 가야 하는 경우
        c_temp += 1
    elif (down and left) or ((not up) and (not down) and left):  # 위로 가야 하는 경우
        r_temp += 1
    elif (down and right) or ((not left) and (not right) and down) or (not up and not down and not left and not right):  # 왼 쪽으로 가야 하는 경우
        c_temp -= 1

    return r_temp, c_temp

N = int(input())
grid = []
grid_visit = [[False for _ in range(N+2)] for _ in range(N+2)]
SUM = 0
current_position = (N//2, N//2)
previous_position = current_position
for _ in range(N):
        grid.append(list(map(int, input().split())))

while True:
    if current_position == (0, 0):
        break
    current_position = move(previous_position[0], previous_position[1])
    previous_position = current_position
    SUM += 1

print(grid)