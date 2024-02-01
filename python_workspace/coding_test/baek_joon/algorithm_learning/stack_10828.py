n = int(input())

stack = []
inputs = []
for _ in range(n):
    inputs.append(input().split())

for oper in inputs:
    if len(oper) == 2:
        stack.append(oper[1])
    else:
        if oper[0] == "pop":
            if not stack:
                print(-1)
            else:
                print(stack.pop())
        elif oper[0] == "size":
            print(len(stack))
        elif oper[0] == "empty":
            print(1 if not stack else 0)
        elif oper[0] == "top":
            if not stack:
                print(-1)
            else:
                print(stack[-1])