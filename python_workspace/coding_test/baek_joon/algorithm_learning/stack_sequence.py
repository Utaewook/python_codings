n = int(input())

sequence = []
for _ in range(n):
    sequence.append(int(input()))
sequence.reverse()

stack = []
i = 1
val = sequence.pop()

while sequence:
    while i < n + 1:  # pop
        if i == val:
            print('-')
            stack.pop()
            val = sequence.pop()
        else:  # push
            print('+')
            stack.append(i)
            i += 1

