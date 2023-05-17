import sys
input = sys.stdin.readline

N,M = map(int,input().split())

nums = list(map(int,input().split()))
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + nums[i]

for _ in range(M):
    x,y = map(int,input().split())
    print(prefix_sum[y] - prefix_sum[x - 1])