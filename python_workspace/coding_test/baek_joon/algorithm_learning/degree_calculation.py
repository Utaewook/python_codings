def dfs(x,y):
    global path, result

    for next_x in relates[x]:
        if next_x == y:
            result = len(path) + 1
            return
        if not visited[next_x]:
            visited[next_x] = True
            path.append(next_x)
            dfs(next_x, y)
            visited[next_x] = False
            path.pop()


n = int(input())

a, b = map(int,input().split())
relates = {i: [] for i in range(n+1)}
visited = [False]*(n+1)
path = []
result = -1

for _ in range(int(input())):
    parent, child = map(int,input().split())
    relates[parent].append(child)
    relates[child].append(parent)

dfs(a, b)

print(result)