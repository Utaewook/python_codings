T = int(input())

for test_case in range(1, T+1):
    N, M = map(int,input().split())
    area = [list(map(int,input().split())) for _ in range(N)]
    max_val = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            max_val = max(max_val, sum([area[k][l] for k in range(i,i+M) for l in range(j,j+M)]))
    print(f"#{test_case} {max_val}")