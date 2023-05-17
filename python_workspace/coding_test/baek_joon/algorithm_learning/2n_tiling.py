n = int(input())

mem = {0:0, 1:1, 2:2}

def dp(i):
    if i not in mem:
        mem[i] = dp(i-1) + dp(i-2)
    return mem[i]

print(dp(n)%10007)