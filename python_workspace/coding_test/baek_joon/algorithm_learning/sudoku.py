# def get_square(i, j):
#     global problem
#     pos_idx = [(0, 1, 2),
#                (3, 4, 5),
#                (6, 7, 8)]
#     i_pos, j_pos = i // 3, j // 3
#     result = set()
#
#     for a in pos_idx[i_pos]:
#         for b in pos_idx[j_pos]:
#             if problem[a][b]:
#                 result.add(problem[a][b])
#
#     return result
#
#
# def dfs():
#     global problem, blanks
#
#     if not blanks:
#         return True
#
#     curr_r, curr_c = blanks.pop()
#
#     line_ver, line_hor, square = set([problem[i][curr_c] for i in range(9)]), set(problem[curr_r]), get_square(curr_r,
#                                                                                                                curr_c)
#     candidates = num_range - line_ver - line_hor - square
#
#     if candidates:
#         for candidate in candidates:
#             problem[curr_r][curr_c] = candidate
#             if dfs():
#                 return True
#             problem[curr_r][curr_c] = 0
#     else:
#         blanks.append((curr_r, curr_c))
#
#     return False
#
# problem = [list(map(int, input().split())) for _ in range(9)]
# blanks = [(i, j) for i in range(9) for j in range(9) if not problem[i][j]]
# num_range = set([d for d in range(1, 10)])
# dfs()
#
# for row in problem:
#     print(*row)


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

    def backtrack(index):
        if index == len(empty_cells):
            return True

        row, col = empty_cells[index]
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                if backtrack(index + 1):
                    return True
                board[row][col] = 0

        return False

    backtrack(0)
    return board
# Example usage:
sudoku_board = [list(map(int, input().split())) for _ in range(9)]

solved_board = solve_sudoku(sudoku_board)
for row in solved_board:
    print(*row)