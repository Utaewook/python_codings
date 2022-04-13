
def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        pop_idx = -1
        li = [i[move - 1] for i in board]
        for idx in range(len(li)):
            if li[idx] != 0:
                pop_idx = idx
                break

        if pop_idx != -1:
            if len(stack) > 0 and board[pop_idx][move-1] == stack[len(stack)-1]:
                stack.pop()
                answer += 1
            else:
                stack.append(board[pop_idx][move-1])
            board[pop_idx][move - 1] = 0
    return answer * 2

test_case = ([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])

print(solution(test_case[0],test_case[1]))