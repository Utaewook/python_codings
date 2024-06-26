def hanoi(n, start, through, to):
    if n > 0:
        global count, moves
        hanoi(n-1, start, to, through)
        moves.append([start, to])
        count += 1
        hanoi(n-1, through, start, to)


count = 0
moves = list()
num = int(input())
hanoi(num, '1','2','3')
print(count)
for m in moves:
    print(*m)