# def dfs(idx1, idx2, stack):
#     global s1, s2, answer
#
#     if idx1 >= len(s1) or idx2 >= len(s2):
#         answer = max(answer, len(stack))
#         return
#
#     if s1[idx1] == s2[idx2]:
#         stack.append(s1[idx1])
#         dfs(idx1 + 1, idx2 + 1, stack)
#         stack.pop()
#     else:
#         dfs(idx1+1, idx2, stack)
#         dfs(idx1, idx2+1, stack)
#
#
# if __name__ == '__main__':
#     import sys
#
#     fast_input = sys.stdin.readline
#
#     s1, s2 = list(fast_input().strip()), list(fast_input().strip())
#
#
#     answer = 0
#     dfs(0,0,[])
#     print(answer)

import sys
fast_input = sys.stdin.readline

s1, s2 = list(fast_input().strip()), list(fast_input().strip())

dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2,)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
