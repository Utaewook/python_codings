T = int(input())

for test_case in range(1,T+1):
    board = [list(input()) for _ in range(8)]
    result = 'yes'
    for i in range(8):
        if board[i].count('O') == 1:
            idx = board[i].index('O')
            check_list = [board[i][n] for n in range(8) if n!=idx] + [board[n][idx] for n in range(8) if n!=i]
            if 'O' in check_list:
                result = 'no'
                break
        else:
            result = 'no'
            break
    print("#{} {}".format(test_case,result))
