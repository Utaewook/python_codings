from collections import deque

seats = [list(input()) for _ in range(5)]
visited = [[False for _ in range(5)] for _ in range(5)]

result = set()
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)  # 상하좌우 순서로 움직임

def bt(r,c):
    queue = deque()
    queue.append((r,c))
    stack = list()

    print(f'bt start at ({r}, {c})')
    while queue:
        pass



def Y_count(coords):
    count = 0
    for r, c in coords:
        if seats[r][c] == 'Y':
            count += 1
    return count


for i in range(5):
    for j in range(5):
        bt(i, j)

print(result)
print(len(result))
