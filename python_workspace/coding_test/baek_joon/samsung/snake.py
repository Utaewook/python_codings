n = int(input())
apple = []
for _ in range(int(input())):
    apple.append(tuple(*map(int,input().split())))

dir = []
for _ in range(int(input())):
    sec, d = input().split()
    dir.append((int(sec),d))

game_sec = 0
curr_dir = 1
def move(x,y,d):
    if d == 'L':
        pass