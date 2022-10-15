n = int(input())

apple = []
for _ in range(int(input())):
    row, col = map(int, input().split())
    apple.append([row - 1, col - 1])

dir = {}
for _ in range(int(input())):
    sec, d = input().split()
    dir[int(sec)] = d

vector = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 상하좌우 움직이기 (편의를 위해 우 - 하 - 좌 - 상 순으로 배열)
game_sec = 0
curr_dir = 0

snake = [[0, 0]]  # 뱀의 위치를 나타내는 좌표들 인덱스 0번엔 머리가 있고 마지막에는 tail이 있다

while True:
    # 뱀의 머리를 한칸 늘린다
    next_head = [snake[0][0] + vector[curr_dir][0], snake[0][1] + vector[curr_dir][1]]

    # 머리가 몸에 부딪히거나 벽에 닿는 경우
    if next_head in snake or next_head[0] >= n or next_head[0] <= -1 or next_head[1] >= n or next_head[1] <= -1:
        game_sec += 1
        break
    elif next_head in apple:  # 머리가 사과를 먹는경우
        snake = [next_head] + snake  # 머리를 늘려주고
        apple.remove(next_head)  # 사과 먹은거 없애줌
    else:  # 그냥 앞으로 간 경우
        snake = [next_head] + snake  # 머리를 늘려주고
        snake.pop()  # 꼬리 줄여주기

    game_sec += 1

    if game_sec in dir.keys():
        if dir[game_sec] == "D":  # 오른쪽으로 90도 회전
            curr_dir = (curr_dir + 1) % 4
        else:  # 왼쪽으로 90도 회전
            curr_dir = (curr_dir + 3) % 4

print(game_sec)
