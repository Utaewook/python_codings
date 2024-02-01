
def solution(rc, operations):
    answer = rc
    for operation in operations:
        if operation == "Rotate":
            answer = rotate(answer)
        elif operation == "ShiftRow":
            answer = shiftrow(answer)

    return answer


def shiftrow(rc):
    return rc[1:]+rc[:-1]


def rotate(rc):
    answer = rc
    array_0_row = [rc[1][0]] + rc[0][:-1]
    array_last_col = [rc[0][-2]] + rc[:-1][-1]
    array_last_row = rc[-1][1:] + [rc[-2][-1]]
    array_0_col = rc[1:][0] + [rc[-1][1]]

    answer[0] = array_0_row
    answer[-1] = array_last_row
    for i in range(len(rc)):
        answer[i][0] = array_0_col[i]
        answer[i][-1] = array_last_col[i]

    return answer


test_cases = ([[[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]], ["Rotate", "ShiftRow"]],
              [[[8, 6, 3],
                [3, 3, 7],
                [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]],
              [[[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]])
count = 1
for test_case in test_cases:
    print(f"{count}번째 test case")
    print(solution(test_case[0],test_case[1]))
    count += 1