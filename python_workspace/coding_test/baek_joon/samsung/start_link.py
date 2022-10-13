import sys
input = sys.stdin.readline

N = int(input())

stats = [[*map(int, input().split())] for _ in range(N)]
players = [None] * N
answer = 100000000

def dfs(count, pos):
    global answer
    if count == N//2:
        start = link = 0
        for i in range(N):
            for j in range(N):
                if players[i] and players[j]:
                    start += stats[i][j]
                if not players[i] and not players[j]:
                    link += stats[i][j]

        if answer > abs(start-link):
            answer = abs(start-link)
        return

    for i in range(pos,N):
        players[i] = True
        dfs(count+1,i+1)
        players[i] = False


dfs(0,1)

print(answer)