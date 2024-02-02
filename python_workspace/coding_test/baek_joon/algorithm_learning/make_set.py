import sys

input = sys.stdin.readline
s = [0] * 21

for _ in range(int(input())):
    line = input().rstrip()
    if ' ' in line:
        op, x = line.split()
        x = int(x)
    else:
        op = line

    if op == 'add':
        s[x] = 1
    elif op == 'remove':
        s[x] = 0
    elif op == 'check':
        print(s[x])
    elif op == 'toggle':
        s[x] = 1 - s[x]
    elif op == 'all':
        s = [1] * 21
    else:
        s = [0] * 21