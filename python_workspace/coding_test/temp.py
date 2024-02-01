# def combinations(arr, r):
#     n = len(arr)
#     result = []
#     count = 0
#
#     def dfs(idx):
#         nonlocal count
#
#         if count == r:
#             print(result)
#             return
#
#         if idx == n:
#             return
#
#         # 현재 원소 선택
#         result.append(arr[idx])
#         count += 1
#         dfs(idx + 1)
#
#         # 현재 원소 선택 안 함
#         result.pop()
#         count -= 1
#         dfs(idx + 1)
#
#     dfs(0)
#
#
#
# combinations([i for i in range(6)],2)

from collections import deque

n = int(input())

maze = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]


def print_matrix(array):
    print()
    for i in range(len(array)):
        print(*array[i])

    print()


def bfs(start_r, start_c):
    queue = deque()
    queue.append((start_r, start_c))
    maze[start_r][start_c] = 1
    path = []

    dr = (1, -1, 0, 0)
    dc = (0, 0, -1, 1)

    while queue:
        curr_r, curr_c = queue.popleft()
        visited[curr_r][curr_c] = True
        for i in range(4):
            next_r = curr_r + dr[i]
            next_c = curr_c + dc[i]
            print(queue)
            print(next_r, next_c)

            if next_r in [-1, n] or next_c in [-1, n]:
                continue
            if not visited[next_r][next_c]:
                queue.append((next_r, next_c))
                maze[next_r][next_c] = 1
                path.append((next_r, next_c))
    return path


result = bfs(0, 0)
print_matrix(maze)

print(result)
