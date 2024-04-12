n, m = map(int,input().split())
board = [list(input()) for _ in range(n)]
min_val = 64

for i in range(n - 7):
    for j in range(m - 7):
        count = 0
        left_top = board[i][j]

        for row in range(i, i+8):
            for col in range(j, j+8):
                if (row+col) % 2 == 0 and board[row][col] != left_top:
                    count += 1
                elif (row+col) % 2 == 1 and board[row][col] == left_top:
                    count += 1

        min_val = min([min_val, count, 64 - count])

print(min_val)