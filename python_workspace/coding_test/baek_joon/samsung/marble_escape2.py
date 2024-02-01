n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

# 상하좌우 이동 방향
dir = ((-1, 0), (1, 0), (0, -1), (0, 1))

wall = set()
way = set()
red = (False, False)
blue = (False, False)
out = (False, False)

for i in range(n):
    for j in range(m):
        position = (i,j)
        if board[i][j] == '#':
            wall.add(position)
        elif board[i][j] == '.':
            way.add(position)
        elif board[i][j] == 'R':
            red = position
        elif board[i][j] == 'B':
            blue = position
        elif board[i][j] == 'O':
            out = position


def is_RB_neighbor(pos_r, pos_b):
    for dr,dc in dir:
        p = (pos_r[0] + dr, pos_r[0] + dc)
        if p == pos_b:
            return True
    return False



def move():

    pass


for count in range(1,11):
    pass