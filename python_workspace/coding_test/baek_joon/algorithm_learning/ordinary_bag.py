N, K = map(int,input().split())

items = list(tuple(map(int,input().split())) for _ in range(N))

# dp 배열 초기화: 물건이 없거나, 무게 제한이 0인 경우를 고려하여 모두 0으로 설정
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# DP를 이용하여 문제 해결
for i in range(1, N + 1):
    for w in range(1, K + 1):
        if items[i - 1][0] <= w:  # i번째 물건을 배낭에 넣을 수 있는 경우
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][0]] + items[i - 1][1])
        else:  # i번째 물건을 배낭에 넣을 수 없는 경우
            dp[i][w] = dp[i - 1][w]

print(dp[N][K])