# import sys
#
# input = sys.stdin.readline
# sys.setrecursionlimit(int(1e5))

# 첫째 줄에 노드의 개수 N과 거리를 알고 싶은 노드 쌍의 개수 M이 입력되고
# # 다음 N-1개의 줄에 트리 상에 연결된 두 점과 거리(10,000 이하의 정수)를 입력받는다.
# # 그 다음 줄에는 거리를 알고 싶은 M개의 노드 쌍이 한 줄에 한 쌍씩 입력된다.
#
# n, m = map(int, input().split())
# tree_distance = {}
# tree = {}
# visited = []
# path = []
#
#
# def dfs(x, y): # x에서 y로 가는 길을 탐색하는 dfs
#     print(path)
#     go_for = tree[x]
#
#     for next_x in go_for:
#         if y == next_x:
#             path.append(next_x)
#             return
#         if next_x >= n or next_x <= -1:
#             continue
#         if not visited[next_x]:
#             visited[next_x] = True
#             path.append(next_x)
#             dfs(next_x,y)
#
#
# def init():
#     global visited
#     global path
#     visited = [False for _ in range(n)]
#     path = []
#
#
# for _ in range(n - 1):
#     a, b, d = map(int, input().split())
#     tree_distance[(a, b)] = d
#     tree_distance[(b, a)] = d
#     if a not in tree.keys():
#         tree[a] = [b]
#     else:
#         tree[a].append(b)
#     if b not in tree.keys():
#         tree[b] = [a]
#     else:
#         tree[b].append(a)
#
# answer = []
# for _ in range(m):
#     x, y = map(int, input().split())
#     init()
#     path.append(x)
#     if not visited[x]:
#         dfs(x,y)
#
#     distance = 0
#     for i in range(len(path) - 1):
#         distance += tree_distance[(path[i],path[i+1])]
#
# for i in range(m):
#     print(answer[i])

import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]


def dfs(x):
    for data in graph[x]:
        y = data[0]
        cost = data[1]
        if not visited[y]:
            visited[y] = True
            distance[y] = distance[x] + cost
            dfs(y)


for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

answer = []
for i in range(m):
    x, y = map(int, input().split())
    visited = [False] * (n + 1)
    distance = [-1] * (n + 1)
    visited[x] = True
    distance[x] = 0
    dfs(x)
    answer.append(distance[y])

for i in range(len(answer)):
    print(answer[i])
