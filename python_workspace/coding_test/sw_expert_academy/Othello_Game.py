T = int(input())

d=((1,0),(0,1),(-1,0),(0,-1),
     (1,-1),(-1,1),(1,1),(-1,-1))


for test_case in range(1, T+1):
    N, M = map(int,input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    board[N//2][N//2-1],board[N//2-1][N//2],board[N//2-1][N//2-1],board[N//2][N//2] = 1,1,2,2
    for _ in range(M):
        r,c,stone = map(int,input().split())
        print(r-1,c-1,stone,"\nbefore")
        for b in board:
            print(*b)
        print()
        board[r-1][c-1] = stone

        for i in range(8):
            next_r,next_c = r-1+d[i][0],c-1+d[i][1]
            if next_r in [-1,N] or next_c in [-1,N] or board[next_r][next_c] == 0 or board[next_r][next_c] == stone:
                continue
            stack = []
            stack.append((next_r,next_c))
            while True:
                next_r,next_c = next_r+d[i][0],next_c+d[i][1]
                if next_r in [-1,N] or next_c in [-1,N] or board[next_r][next_c] == 0 or (board[next_r][next_c] == stone and board[stack[-1][0]][stack[-1][1]] == stone):
                    break
                elif board[next_r][next_c] == stone and board[stack[-1][0]][stack[-1][1]] not in [stone,0]:
                    stack.append((next_r,next_c))
                    break

                stack.append((next_r,next_c))
            print(stack,[board[rr][cc] for rr,cc in stack])
            if stack:
                nr,nc = stack.pop()
                temp_stack = [board[rr][cc] for rr,cc in stack]
                if board[nr][nc] == stone and stone not in temp_stack:
                    for tr,tc in stack:
                        board[tr][tc] = stone
        print("after")
        for b in board:
            print(*b)
        print()

    w_count, b_count = 0,0
    for b in board:
        b_count += b.count(1)
        w_count += b.count(2)
    print(f"#{test_case} {b_count} {w_count}")
