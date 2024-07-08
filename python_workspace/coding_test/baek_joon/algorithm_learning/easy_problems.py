n = int(input())
tree = list(list(map(int,input().split())) for _ in range(n))

memo = [[0]*i for i in range(1, n+1)]
memo[0][0] = tree[0][0]

for level in range(1, len(tree)):
    for i in range(level + 1):
        if i - 1 < 0:
            memo[level][i] = memo[level-1][i] + tree[level][i]
        elif i > level-1:
            memo[level][i] = memo[level-1][i-1] + tree[level][i]
        else:
            memo[level][i] = max(memo[level-1][i-1], memo[level-1][i]) + tree[level][i]

print(max(memo[-1]))

