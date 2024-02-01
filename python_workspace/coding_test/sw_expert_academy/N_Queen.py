T = int(input())

for test_case in range(1,T+1):
    N = int(input())


    # x번째 행에 놓은 퀸에 대해 검증
    def check(x):
        for i in range(x):  # 이전 행에서 놓았던 모든 퀸들을 확인
            if row[x] == row[i]:  # 위쪽 확인
                return False
            if abs(row[x] - row[i]) == x - i:  # 대각선 확인
                return False
        return True


    def dfs(x):  # x번째 행에 대하여 처리
        global result
        if x == N:
            result += 1
        else:  # x 번쨰 행의 각 열에 퀸을 둔다고 가정
            for i in range(N):
                row[x] = i
                if check(x):
                    dfs(x + 1)  # 다음행으로
    row = [0] * N
    result = 0
    dfs(0)
    print(f'#{test_case} {result}')