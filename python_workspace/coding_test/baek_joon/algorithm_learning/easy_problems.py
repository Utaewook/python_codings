n = int(input())
wines = list(int(input()) for _ in range(n))

dp = [[0] * 4 for _ in range(n)]
dp[0] = [0, 0, wines[0], wines[0]]

for i in range(1, n):
    dp[i] = [max(dp[i-1][0:2]),
             max(dp[i-1][2:]),
             max(dp[i-1][0:2]) + wines[i],
             dp[i-1][2] + wines[i]]

print(max(dp[n-1]))