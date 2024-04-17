import sys
input = sys.stdin.readline

stack = list()

for _ in range(int(input())):
    line = input().rstrip()

    if len(line) != 1:
        op, n = map(int, line.split())
        stack.append(n)

    elif line == '2':
        if stack:
            n = stack.pop()
            print(n)
        else:
            print(-1)
    elif line == '3':
        print(len(stack))
    elif line == '4':
        print(1 if not stack else 0)
    else:
        print(-1 if not stack else stack[-1])
