import sys

input = sys.stdin.readline

ps = {"{": "}", "[": "]", "(": ")"}

while True:
    line = input().rstrip()

    if line == '.':
        break

    stack = list()
    line = list(line)
    for s in line:
        if (s not in ps) and (s not in ps.values()):
            continue

        if not stack or s in ps:
            stack.append(s)
        else:
            if stack[-1] in ps and ps[stack[-1]] == s:
                stack.pop()
            elif s in ps.values():
                stack.append(s)

    if stack:
        print('no')
    else:
        print('yes')
