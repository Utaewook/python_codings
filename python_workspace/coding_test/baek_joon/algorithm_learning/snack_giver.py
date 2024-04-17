import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
stack = list()
enter_num = 1

for i in nums:
    if i == enter_num:
        enter_num += 1
        continue

    while stack and stack[-1] == enter_num:
        stack.pop()
        enter_num += 1
    stack.append(i)

while (enter_num <= n) and stack:
    if stack[-1] == enter_num:
        stack.pop()
    enter_num += 1

print("Sad" if stack else "Nice")