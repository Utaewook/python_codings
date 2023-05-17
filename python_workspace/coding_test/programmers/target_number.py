def solution(numbers, target):
    answer = 0

    def dfs(selected):
        nonlocal answer
        if len(selected) == len(numbers):
            res = 0
            for i in range(len(numbers)):
                if selected[i] == '-':
                    res -= numbers[i]
                else:
                    res += numbers[i]
            if res == target:
                answer += 1
            return

        dfs(selected+['+'])
        dfs(selected+['-'])

    dfs([])

    return answer

print(solution())