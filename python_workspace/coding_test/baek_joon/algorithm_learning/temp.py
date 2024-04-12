# # test_cases = int(input())
# #
# # for test_case in range(test_cases):
# #     days = int(input())
# #     cost = list(map(int, input().split()))
# #     cost.reverse()
# #     stock_stack = []
# #     profit = 0
# #     while cost:
# #         c = cost.pop()
# #         if (not stock_stack) or stock_stack[-1] <= c:
# #             stock_stack.append(c)
# #         elif stock_stack[-1] > c:
# #             profit += stock_stack[-1] * (len(stock_stack) - 1) - sum(stock_stack[:-1])
# #             stock_stack = [c]
# #     if stock_stack:
# #         profit += stock_stack[-1] * (len(stock_stack) - 1) - sum(stock_stack[:-1])
# #
# #
# #     print(f"#{test_case + 1} {profit}")
# #
# # def solution(numbers):
# #     answer = set()
# #     numbers = list(numbers)
# #     for i in range(1, len(numbers) + 1):
# #         answer.update(permutation(numbers, i))
# #     print(answer)
# #
# #     return len(answer)
# #
# #
# # def is_prime(n):
# #     if n < 2:
# #         return False
# #     for i in range(2, int(n ** 0.5) + 1):
# #         if n % i == 0:
# #             return False
# #     return True
# #
# #
# # def permutation(arr, n):
# #     result = set()
# #
# #     def dfs(selected, rest):
# #         if len(selected) == n:
# #             s = ''.join(selected)
# #             if is_prime(int(s)):
# #                 result.add(int(s))
# #
# #         for i in range(len(rest)):
# #             selected.append(rest[i])
# #             dfs(selected, rest[:i] + rest[i + 1:])
# #             selected.pop()
# #
# #     dfs([], arr[:])
# #     return result
# #
# # print(solution("17"))
# # print(solution("011"))
# # print(is_prime(17))
#
# n = int(input())
# mem = {0: 1, 1: 1, 2: 2}
#
#
# def factorial(i):
#     if i not in mem:
#         mem[i] = factorial(i - 1) * i
#     return mem[i]
#
# print(factorial(n))

check = set(range(1, 31))

for _ in range(m):
    n = int(input())
    check.remove(n)

print(min(check))
print(max(check))
