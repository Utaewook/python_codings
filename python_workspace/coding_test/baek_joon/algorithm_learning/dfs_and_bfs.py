from collections import deque


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)


def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        curr_v = queue.popleft()
        if not visited[curr_v]:
            print(curr_v, end=' ')
        visited[curr_v] = True
        for next_v in graph[curr_v]:
            if not visited[next_v]:
                queue.append(next_v)


N, M, V = map(int,input().split())

graph = {i:[] for i in range(N + 1)}
visited = [False for _ in range(N + 1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    graph[g].sort()

dfs(V)
print()
visited = [False for _ in range(N + 1)]
bfs(V)