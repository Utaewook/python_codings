from collections import deque

def bfs(v):
    queue = deque()

    queue.append(v)
    while queue:
        curr_computer = queue.popleft()
        visited[curr_computer] = True
        for next_computer in network[curr_computer]:
            if not visited[next_computer]:
                queue.append(next_computer)


N = int(input())
V = int(input())

network = {i:[] for i in range(N+1)}
visited = [False for _ in range(N+1)]

for _ in range(V):
    a,b = map(int,input().split())
    network[a].append(b)
    network[b].append(a)

bfs(1)
print(visited.count(True) - 1)
