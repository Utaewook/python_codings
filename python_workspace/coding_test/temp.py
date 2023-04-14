# def combinations(arr, r):
#     n = len(arr)
#     result = []
#     count = 0
#
#     def dfs(idx):
#         nonlocal count
#
#         if count == r:
#             print(result)
#             return
#
#         if idx == n:
#             return
#
#         # 현재 원소 선택
#         result.append(arr[idx])
#         count += 1
#         dfs(idx + 1)
#
#         # 현재 원소 선택 안 함
#         result.pop()
#         count -= 1
#         dfs(idx + 1)
#
#     dfs(0)
#
#
#
# combinations([i for i in range(6)],2)

import time

s = '*'
N = 100000000

array = []
string = ''

start = time.time()
for _ in range(N):
    array.append(s)
print(f"array append = {time.time()-start}")

start = time.time()
tup = tuple(array)
print(f"array to tuple = {time.time()-start}")

start = time.time()
for _ in range(N):
    string = string.join(s)
print(f"string join = {time.time()-start}")

string = ''
start = time.time()
for _ in range(N):
    string += s
print(f"string + = {time.time()-start}")