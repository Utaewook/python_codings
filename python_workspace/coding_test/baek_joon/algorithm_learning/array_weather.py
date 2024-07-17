import sys
fast_input = sys.stdin.readline

n, k = map(int,input().split())
nums = list(map(int,input().split()))

sums = [0] * n
sums[0] = nums[0]

for i in range(1, n):
    sums[i] = nums[i] + sums[i-1]

val_max = - 101

for i in range(n-k):
    val_max = max(val_max, sums[i+k] - sums[i])

print(val_max)