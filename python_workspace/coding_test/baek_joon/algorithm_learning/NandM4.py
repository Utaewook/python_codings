n, m = map(int,input().split())

state = []

def bt():
    if len(state) == m:
        print(' '.join(map(str, state)))
        return
    for i in range(1, n + 1):
        if state and state[-1] > i:
            continue
        state.append(i)
        bt()
        state.pop()

bt()