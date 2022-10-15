# import itertools
#
#
# def cal_(a, b, op):
#     if op == '+':
#         return a + b
#     elif op == '-':
#         return a - b
#     elif op == '*':
#         return a * b
#     elif op == '/':
#         if a < 0 < b:
#             return -1 * ((a * -1) // b)
#         else:
#             return a // b
#
#
# n = int(input())
# nums = list(map(int, input().split()))
# operator_inputs = list(map(int, input().split()))
#
# results = []
# operators = [*['+'] * operator_inputs[0],
#              *['-'] * operator_inputs[1],
#              *['*'] * operator_inputs[2],
#              *['/'] * operator_inputs[3]]
#
# s = set()
# for op in itertools.permutations(operators, len(operators)):
#     s.add(op)
#
# count = 0
# for op in s:
#     res = 0
#     for i in range(len(nums) - 1):
#         if i == 0:
#             res = cal_(nums[i], nums[i + 1], op[i])
#         else:
#             res = cal_(res, nums[i + 1], op[i])
#     results.append(res)
#     count += 1
#
# print(max(results), results.index(max(results)))
# print(min(results), results.index(min(results)))

#  dfs brute force

def dfs(depth, res):
    global MAX
    global MIN

    if depth == n:
        MAX = max(MAX, res)
        MIN = min(MIN, res)

    if operator_inputs[0] != 0:
        operator_inputs[0] -= 1
        dfs(depth + 1, res + nums[depth])
        operator_inputs[0] += 1

    if operator_inputs[1] != 0:
        operator_inputs[1] -= 1
        dfs(depth + 1, res - nums[depth])
        operator_inputs[1] += 1

    if operator_inputs[2] != 0:
        operator_inputs[2] -= 1
        dfs(depth + 1, res * nums[depth])
        operator_inputs[2] += 1

    if operator_inputs[3] != 0:
        operator_inputs[3] -= 1
        if res < 0 < nums[depth]:
            dfs(depth + 1, -1 * ((-1 * res) // nums[depth]))
        else:
            dfs(depth + 1, res // nums[depth])
        operator_inputs[3] += 1


n = int(input())
nums = list(map(int, input().split()))
operator_inputs = list(map(int, input().split()))

MAX = -1e9
MIN = 1e9

dfs(1, nums[0])

print(MAX)
print(MIN)
