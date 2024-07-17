def get_square(i, j):
    global problem
    pos_idx = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    i_pos, j_pos = i // 3, j // 3
    result = set()

    for a in pos_idx[i_pos]:
        for b in pos_idx[j_pos]:
            if problem[a][b]:
                result.add(problem[a][b])

    return result

def dfs():
    global problem, blanks

    if not blanks:
        return True

    curr_r, curr_c = blanks[-1]

    line_ver = set(problem[i][curr_c] for i in range(9))
    line_hor = set(problem[curr_r])
    square = get_square(curr_r, curr_c)
    candidates = num_range - line_ver - line_hor - square

    if candidates:
        for candidate in candidates:
            problem[curr_r][curr_c] = candidate
            blanks.pop()
            if dfs():
                return True
            problem[curr_r][curr_c] = 0
            blanks.append((curr_r, curr_c))
    else:
        return False

    return False

# 문제 입력 받기
problem = [list(map(int, input().split())) for _ in range(9)]
blanks = [(i, j) for i in range(9) for j in range(9) if not problem[i][j]]
num_range = set(range(1, 10))

dfs()

for row in problem:
    print(*row)
