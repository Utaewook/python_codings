from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [False] * (F+1)


def bfs():
    if G == S:
        return 0
    temp = set()
    temp.add(S)
    count = 0

    while temp:
        queue = deque(temp)
        temp = set()
        count += 1
        while queue:
            curr_s = queue.popleft()
            visited[curr_s] = True
            if curr_s+U == G or curr_s-D == G:
                return count
            else:
                if curr_s+U < F and not visited[curr_s+U]:
                    temp.add(curr_s+U)
                if curr_s-D > 0 and not visited[curr_s-D]:
                    temp.add(curr_s-D)
    return "use the stairs"


print(bfs())