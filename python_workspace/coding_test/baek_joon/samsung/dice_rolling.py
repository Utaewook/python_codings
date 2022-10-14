n, m, row, col, command = map(int, input().split())
MAP = []
dice = [0] * 6
curr_r, curr_c = row, col
for _ in range(n):
    MAP.append(list(map(int, input().split())))

command = list(map(int, input().split()))
dice_dir = ['t', 'n', 'e', 'w', 's', 'b']

for i in range(len(command)):
    top, east, west, bottom, north, south = dice_dir.index('t'), dice_dir.index('e'), dice_dir.index('w'), dice_dir.index('b'), dice_dir.index('n'), dice_dir.index('s')
    if command[i] == 1:  # 동쪽으로 굴리기
        if curr_c + 1 == m:
            continue
        dice_dir[top] = 'e'; dice_dir[east] = 'b'; dice_dir[bottom] = 'w'; dice_dir[west] = 't'
        curr_c += 1
    elif command[i] == 2:  # 서쪽으로 굴리기
        if curr_c - 1 == -1:
            continue
        dice_dir[top] = 'w'; dice_dir[west] = 'b'; dice_dir[bottom] = 'e'; dice_dir[east] = 't'
        curr_c -= 1
    elif command[i] == 3:  # 북쪽으로 굴리기
        if curr_r - 1 == -1:
            continue
        dice_dir[top] = 'n'; dice_dir[north] = 'b'; dice_dir[bottom] = 's'; dice_dir[south] = 't'
        curr_r -= 1
    elif command[i] == 4:  # 남쪽으로 굴리기
        if curr_r + 1 == n:
            continue
        dice_dir[top] = 's'; dice_dir[south] = 'b'; dice_dir[bottom] = 'n'; dice_dir[north] = 't'
        curr_r += 1

    bottom = dice_dir.index('b')
    top = dice_dir.index('t')
    if MAP[curr_r][curr_c] != 0:
        dice[bottom] = MAP[curr_r][curr_c]
        MAP[curr_r][curr_c] = 0
    else:
        MAP[curr_r][curr_c] = dice[bottom]
    print(dice[top])
