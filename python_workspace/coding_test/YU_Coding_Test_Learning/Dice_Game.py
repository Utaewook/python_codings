N = int(input())

games = []

for _ in range(N):
    a, b, c = map(int, input().split())
    if a == b and b == c:
        games.append(10000 + a * 1000)
    elif a == b and b != c:
        games.append(1000 + a * 100)
    elif b == c and c != a:
        games.append(1000 + b * 100)
    elif c == a and a != b:
        games.append(1000 + c * 100)
    else:
        games.append(max([a, b, c]) * 100)

print(max(games))
