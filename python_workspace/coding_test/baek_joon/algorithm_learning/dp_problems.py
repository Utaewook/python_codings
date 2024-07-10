# # 포도주
#
# n = int(input())
# wines = list(int(input()) for _ in range(n))
#
# dp = [[0] * 4 for _ in range(n)]
# dp[0] = [0, 0, wines[0], wines[0]]
#
# for i in range(1, n):
#     dp[i] = [max(dp[i-1][0:2]),
#              max(dp[i-1][2:]),
#              max(dp[i-1][0:2]) + wines[i],
#              dp[i-1][2] + wines[i]]
#
# print(max(dp[n-1]))


# 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))