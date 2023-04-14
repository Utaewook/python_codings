# def dfs(color):
#     global step, result
#     if len(step) == N:
#         result = min(result, mem[''.join(step)])
#         return
#     if step and mem[''.join(step)] > result:
#         return
#
#     for c in range(3):
#         if c != color:
#             step.append(str(c))
#             s = ''.join(step)
#             if len(step) == 1:
#                 mem[s] = street[0][c]
#             else:
#                 mem[s] = mem[s[:-1]] + street[len(step)-1][c]
#             dfs(c)
#             step.pop()
#
#
# N = int(input())
# street = []
# step = []
# mem = {}
# result = 1000 * N
#
# for i in range(N):
#     street.append(tuple(map(int, input().split())))
#
#
# dfs(0)
# dfs(1)
# dfs(2)
#
# print(result)


# dp!!!
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
ans = [[0] * 3 for _ in range(n + 1)]
for i in range(1, n + 1):
    ans[i][0] = min(ans[i - 1][1], ans[i - 1][2]) + dp[i - 1][0]
    ans[i][1] = min(ans[i - 1][0], ans[i - 1][2]) + dp[i - 1][1]
    ans[i][2] = min(ans[i - 1][0], ans[i - 1][1]) + dp[i - 1][2]
print(min(ans[n][0], ans[n][1], ans[n][2]))
