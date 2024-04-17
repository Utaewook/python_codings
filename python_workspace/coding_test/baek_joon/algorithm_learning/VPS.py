import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = list(input().rstrip())
    stack = list()
    for c in s:
        if not stack or c == '(':
            stack.append(c)
        else:
            if c == ')' and stack[-1] == '(':
                stack.pop()


    if stack:
        print('NO')
    else:
        print('YES')
