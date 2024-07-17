
def dfs(e,r):
    global visited, rank, count
    visited[r] = True
    count += 1

    rank[r] = count

    for x in e[r]:
        if not visited[x]:
            dfs(e, x)

n, m, start = map(int,input().split())
graph = dict()
for _ in range(m):
    a,b = map(int,input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

for node in graph:
    graph[node].sort(reverse=True)

visited = [False] * (n + 1)
rank = [0] * (n + 1)
count = 0

dfs(graph,start)
for i in range(1, len(rank)):
    print(rank[i])