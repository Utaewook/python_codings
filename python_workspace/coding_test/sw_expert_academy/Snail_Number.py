T = int(input())

d = ((0, 1), (1, 0), (0, -1), (-1, 0))

for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0 for _ in range(N)] for _ in range(N)]
    number = 1
    r, c, dir_i = 0, 0, 0
    while number <= N ** 2:
        snail[r][c] = number
        next_r, next_c = r + d[dir_i][0], c + d[dir_i][1]
        if next_r in [-1, N] or next_c in [-1, N] or snail[next_r][next_c] != 0:
            dir_i = (dir_i + 1) % 4
            next_r, next_c = r + d[dir_i][0], c + d[dir_i][1]

        number += 1
        r, c = next_r, next_c
    print(f"#{test_case}")
    for s in snail:
        print(*s)
