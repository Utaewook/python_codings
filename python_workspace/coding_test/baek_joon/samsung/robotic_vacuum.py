row, col = map(int, input().split())
r, c, d = map(int, input().split())  # 0,1,2,3 / 북동남서

room = []
for _ in range(row):
    room.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향
row_dir = (-1, 0, 1, 0)
col_dir = (0, 1, 0, -1)


def robot_move(robot_r, robot_c, robot_d):
    room[robot_r][robot_c] = 2  # 현재 위치를 청소한다

    print(robot_r,robot_c)
    for i in range(robot_d + 1, robot_d + 4):
        next_dir = i % 4
        next_row = robot_r + row_dir[next_dir]
        next_col = robot_c + col_dir[next_dir]

        rear_dir = (robot_d + 2) % 4
        rear_row = robot_r + row_dir[rear_dir]
        rear_col = robot_c + col_dir[rear_dir]

        if room[next_row][next_col] == 0:  # 왼쪽 방향에 아직 청소하지 않은 구간이 있다면
            robot_move(next_row, next_col, next_dir)  # 그 방향으로 회전, 한칸 전진
            break
        elif (i == robot_d + 3) and room[rear_row][rear_col] in [2, 0]:
            robot_move(rear_row,rear_col,robot_d)
            break
        elif (i == robot_d + 3) and room[rear_row][rear_col] == 1:
            break
        else:
            continue


robot_move(r,c,d)
for line in room:
    print(line)
print()
print(sum(room, []).count(2))