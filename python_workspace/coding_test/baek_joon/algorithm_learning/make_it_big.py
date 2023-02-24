import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = input().strip()

deleted = 0
stack = list()

for n in num:
    while len(stack) > 0 and stack[-1] < n:
        if deleted == K:
            break
        else:
            stack.pop()
            deleted += 1
    stack.append(n)

for i in range(K-deleted):
    stack.pop()

print(''.join(stack))