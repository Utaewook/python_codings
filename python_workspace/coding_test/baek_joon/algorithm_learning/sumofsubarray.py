n, s = map(int,input().split())

nums = list(map(int, input().split()))

visited = [False] * n

count = 0

def dfs(sum_value, idx):
    global count
    if sum_value+nums[idx] == s:
        count += 1

    if idx == n-1:
        return

    dfs(sum_value, idx+1)
    dfs(sum_value+nums[idx], idx+1)

dfs(0, 0)
print(count)