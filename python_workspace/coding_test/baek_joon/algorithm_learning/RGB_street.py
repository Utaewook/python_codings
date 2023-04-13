# def dfs(color):
#     global step, result
#     if len(step) == N:
#         result = min(result, mem[''.join(step)])
#         return
#     if step and mem[''.join(step)] > result:
#         return
#
#     for c in range(3):
#         if c != color:
#             step.append(str(c))
#             s = ''.join(step)
#             if len(step) == 1:
#                 mem[s] = street[0][c]
#             else:
#                 mem[s] = mem[s[:-1]] + street[len(step)-1][c]
#             dfs(c)
#             step.pop()
#
#
# N = int(input())
# street = []
# step = []
# mem = {}
# result = 1000 * N
#
# for i in range(N):
#     street.append(tuple(map(int, input().split())))
#
#
# dfs(0)
# dfs(1)
# dfs(2)
#
# print(result)


N = int(input())
step = ''
mem = {}
result = 1000 * N

for i in range(N):
    street = tuple(map(int,input().split()))
    for color in range(3):
        step += str(color)
        if len(step) == 1:
            mem[step] = street[color]
        else:
            mem[step] = mem[step[:-1]] + street[color]
        step = step[:-1]


print(result)
