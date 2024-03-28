n, m = map(int,input().split())

visited = [False] * (n + 1)

state = []

def bt():
    if len(state) == m:
        print(' '.join(map(str,state)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            state.append(i)
            bt()
            visited[i] = False
            state.pop()

bt()