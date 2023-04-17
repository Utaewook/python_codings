from collections import deque

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)


def get_iceberg(r, c):
    if ocean[r][c] == 0:
        return
    queue = deque()
    queue.append((r, c))
    iceberg = []

    while queue:
        curr_r, curr_c = queue.popleft()
        melt(curr_r, curr_c)
        print(queue, curr_r, curr_c, f'year {year}')

        for i in range(4):
            next_r, next_c = curr_r + dr[i], curr_c + dc[i]

            if next_r < 0 or next_r >= row or next_c < 0 or next_c >= col:
                continue
            if not visited[next_r][next_c] and ocean[next_r][next_c]:
                queue.append((next_r, next_c))
                visited[next_r][next_c] = True
                iceberg.append((next_r, next_c))

    return tuple(iceberg)


def melt(r, c):
    global ocean, total_ice
    melt_count = 0
    for i in range(4):
        next_r, next_c = r + dr[i], c + dc[i]
        if next_r < 0 or next_r >= row or next_c < 0 or next_c >= col:
            continue
        if ocean[next_r][next_c] == 0:
            melt_count += 1
    ocean[r][c] -= melt_count
    total_ice -= melt_count


row, col = map(int, input().split())

ocean = []
visited = [[False for _ in range(col)] for _ in range(row)]

for _ in range(row):
    ocean.append(list(map(int, input().split())))

total_ice = sum(sum(ocean,[]))
print(total_ice)

year = 0
count_iceberg = 0
while True:

    icebergs = set()
    for x in range(row):
        for y in range(col):
            icebergs.add(get_iceberg(x, y))
    print()
    for a in ocean:
        print(a)
    print()

    if len(icebergs) >= 2:
        print(year)
        break
    if total_ice == 0:
        print(0)
        break
