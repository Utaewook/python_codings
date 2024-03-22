
for test_case in range(int(input())):
    n = int(input())

    sticker = list()
    for i in range(2):
        sticker.append(list(map(int, input().split())))

    # 0: 0번 인덱스 선택
    # 1: 1번 인덱스 선택
    # 2: 선택하지 않음

    mem = [[0, 0, 0] for _ in range(n)]

    mem[0][0] = sticker[0][0]
    mem[0][1] = sticker[1][0]

    for i in range(1, n):
        mem[i][0] = max(mem[i-1][1], mem[i-1][2]) + sticker[0][i]
        mem[i][1] = max(mem[i-1][0], mem[i-1][2]) + sticker[1][i]
        mem[i][2] = max(mem[i-1][0], mem[i-1][1], mem[i-1][2])

    print(max(mem[n-1][0], mem[n-1][1], mem[n-1][2]))