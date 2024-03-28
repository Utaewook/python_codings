n, m = map(int, input().split())

state = []

def dfs():
    if len(state) == m:
        print(' '.join(map(str, state)))
        return
    for i in range(1, n+1):
        state.append(i)
        dfs()
        state.pop()

dfs()