test_cases = [int(input()) for _ in range(int(input()))]

mem = {0:0,1:1,2:2,3:4}

def dp(n):
    if n not in mem:
        val = dp(n-1) + dp(n-2) + dp(n-3)
        mem[n] = val
    return mem[n]

for test_case in test_cases:
    print(dp(test_case))
