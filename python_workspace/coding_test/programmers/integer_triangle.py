def solution(triangle):
    mem = {1: [triangle[0][0]]}

    def dp(n):
        if n not in mem:
            temp = [0 for _ in range(n)]
            prev_dp = dp(n-1)
            temp[0] = prev_dp[0] + triangle[n-1][0]
            temp[-1] = prev_dp[-1] + triangle[n-1][-1]
            for i in range(1, n-1):
                temp[i] = max(prev_dp[i],prev_dp[i-1]) + triangle[n-1][i]
            mem[n] = temp


        return mem[n]


    return max(dp(len(triangle)))


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
print(solution([[1], [1, 2], [1, 1, 3], [9, 1, 8, 1]]))
