import math as m

def move(r, c):
    r_temp, c_temp = r, c
    grid_visit[r+1][c+1] = True
    grid[r][c] = SUM
    up, down, left, right = grid_visit[r][c+1], grid_visit[r+2][c+1], grid_visit[r+1][c], grid_visit[r+1][c+2]
    if (up and right) or ((not up) and (not down) and right):  # 밑으로 가야 하는 경우
        r_temp += 1
    elif (up and left) or ((not left) and (not right) and up):  # 오른 쪽으로 가야 하는 경우
        c_temp += 1
    elif (down and left) or ((not up) and (not down) and left):  # 위로 가야 하는 경우
        r_temp -= 1
    elif (down and right) or ((not left) and (not right) and down) or (not up and not down and not left and not right):  # 왼 쪽으로 가야 하는 경우
        c_temp -= 1

    scatter((r, c), (r_temp, c_temp))
    return r_temp, c_temp

def scatter(x,y):
    global grid
    global SUM
    vector = (y[0]-x[0], y[1]-x[1])
    sand = grid[x[0]][x[1]]
    grid[x[0]][x[1]] = 0
    sand1 = m.floor(sand*(1/100))
    sand2 = m.floor(sand*(2/100))
    sand5 = m.floor(sand*(5/100))
    sand7 = m.floor(sand*(7/100))
    sand10 = m.floor(sand*(10/100))
    sand -= 2*(sand1+sand2+sand7+sand10)+sand5
    if vector == (1, 0):  # 밑으로 이동한 경우
        pass
    elif vector == (-1, 0):  # 위로 이동한 경우
        pass
    elif vector == (0, 1):  # 오른 쪽으로 이동한 경우
        grid[x[0]-1][x[1]] += sand1
        grid[y[0]-1][y[1]] += sand7
        grid[y[0]-2][y[1]] += sand2

    elif vector == (0, -1):  # 왼 쪽으로 이동한 경우
        grid[x[0]+1][x[1]] += sand1
        grid[y[0]+1][y[1]] += sand7
        if y[0]+2 == N:
            SUM += sand2
        else:
            grid[y[0]+2][y[1]] += sand2

        if y[1] == 1:
            SUM += sand5
            grid[y[0]][y[1]-1] += sand
            grid[y[0]+1][y[1]-1] += sand10
            if y[0] == 0:
                SUM += (sand1 + sand2 + sand7 + sand10)
            elif y[0] == 1:
                grid[y[0]-1][y[1]-1] += sand10
                grid[y[0]-1][y[1]] += sand7
                grid[y[0]-1][y[1]+1] += sand1
                SUM += sand2
            else:
                grid[y[0]-1][y[1]-1] += sand10
                grid[y[0]-1][y[1]] += sand7
                grid[y[0]-1][y[1]+1] += sand1
                grid[y[0]-2][y[1]] += sand2
        elif y[1] == 0:
            SUM += (sand + sand5 + sand10 + sand10)
            if y[0] == 0:
                SUM += (sand1 + sand2 + sand7)
            elif y[0] == 1:
                grid[y[0]-1][y[1]+1] += sand1
                SUM += sand2
                grid[y[0]-1][y[1]] += sand7
            else:
                grid[y[0]-1][y[1]+1] += sand1
                grid[y[0]-2][y[1]] += sand2
                grid[y[0]-1][y[1]] += sand7
        else:
            grid[y[0]][y[1]-1] += sand
            grid[y[0]+1][y[1]-1] += sand10
            grid[y[0]][y[1]-2] += sand5
            if y[0] == 0:
                SUM += (sand1 + sand2 + sand7 + sand10)
            elif y[0] == 1:
                grid[y[0]-1][y[1]-1] += sand10
                grid[y[0]-1][y[1]] += sand7
                grid[y[0]-1][y[1]+1] += sand1
                SUM += sand2
            else:
                grid[y[0]-1][y[1]-1] += sand10
                grid[y[0]-1][y[1]] += sand7
                grid[y[0]-1][y[1]+1] += sand1
                grid[y[0]-2][y[1]] += sand2


N = int(input())
grid = []
grid_visit = [[False for _ in range(N+2)] for _ in range(N+2)]
SUM = 0
current_position = (N//2, N//2)
previous_position = current_position
next_position = ()
for _ in range(N):
        grid.append(list(map(int, input().split())))

while True:
    if (current_position[0],current_position[1]+1) == (0, 0):
        break
    current_position = move(previous_position[0], previous_position[1])
    previous_position = current_position

for i in range(N):
    print(grid[i])

for i in range(N+2):
    print(grid_visit[i])