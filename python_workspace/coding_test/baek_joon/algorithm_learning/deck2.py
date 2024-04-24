import sys
from collections import deque
input = sys.stdin.readline

deck = deque()

for _ in range(int(input())):
    line = input().rstrip().split()

    if line[0] == '1':
        deck.appendleft(line[1])
    elif line[0] == '2':
        deck.append(line[1])
    elif line[0] == '3':
        print(deck.popleft() if deck else -1)
    elif line[0] == '4':
        print(deck.pop() if deck else -1)
    elif line[0] == '5':
        print(len(deck))
    elif line[0] == '6':
        print(0 if deck else 1)
    elif line[0] == '7':
        print(deck[0] if deck else -1)
    elif line[0] == '8':
        print(deck[-1] if deck else -1)

