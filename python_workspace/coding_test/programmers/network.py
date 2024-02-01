def solution(n, computers):
    answer = 0
    visited = [False for _ in range(len(computers))]

    def dfs(curr_pc,net):
        for next_pc in range(n):
            if not visited[next_pc] and computers[curr_pc][next_pc] == 1 and next_pc!=curr_pc:
                net.add(next_pc)
                visited[next_pc] = True
                dfs(next_pc,net)


    for i in range(n):
        if not visited[i]:
            dfs(i, set())
            answer += 1
    return answer



test_cases = [[3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]],
              [3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]]]

for test_case in test_cases:
    print(solution(*test_case))