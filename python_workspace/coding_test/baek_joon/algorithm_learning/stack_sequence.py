n = int(input())

sequence = []
for _ in range(n):
    sequence.append(int(input()))
sequence.reverse()
stack = []

i = 1
result = []
while sequence:
    if stack and stack[-1] == sequence[-1]:  # i를 pop
        stack.pop()
        sequence.pop()
        result.append('-')
    else:  # i를 stack에 push 해야 함
        stack.append(i)
        i += 1
        result.append('+')
    if len(result) > 2 * n:
        break


if len(result) > 2 * n:
    print('NO')
else:
    for r in result:
        print(r)