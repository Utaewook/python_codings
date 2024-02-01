from collections import deque

subin, sibling = map(int, input().split())
visited = [False]*100001

def bfs():
    if subin == sibling:
        return 0
    sec = 0
    temp = set()

    temp.add(subin)
    while temp:
        queue = deque(temp)
        temp = set()
        sec += 1
        while queue:
            next_subin = queue.popleft()
            visited[next_subin] = True
            if next_subin + 1 == sibling or next_subin - 1 == sibling or 2 * next_subin == sibling:
                return sec
            elif subin > sibling:
                if next_subin - 1 >= 0 and not visited[next_subin-1]:
                    temp.add(next_subin - 1)
            else:
                if next_subin + 1 <= 100000 and not visited[next_subin+1]:
                    temp.add(next_subin + 1)
                if next_subin - 1 >= 0 and not visited[next_subin-1]:
                    temp.add(next_subin - 1)
                if next_subin * 2 <= 100000 and not visited[next_subin*2]:
                    temp.add(next_subin * 2)


print(bfs())
