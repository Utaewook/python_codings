def solution(ability):
    answer = 0
    visited = [False for _ in range(len(ability[0]) + 1)]

    def dfs(student, s):
        nonlocal answer
        print(student, s)
        if student == 10:
            answer = max(answer, s)
            return

        for idx in range(len(visited)):
            print('\t', idx)
            if visited[idx]:
                continue
            if idx != len(ability[0]):
                visited[idx] = True
                dfs(student + 1, s + ability[student + 1][idx])
                visited[idx] = False
            else:
                dfs(student + 1, s + ability[student + 1][idx])

    dfs(0, 0)

    return answer


print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))