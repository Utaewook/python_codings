n, m = map(int,input().split())

nums = sorted(list(map(int,input().split())))

visited = {num : False for num in nums}

state = []

def bt():
    if len(state) == m:
        print(' '.join(map(str, state)))
        return
    for num in nums:
        if not visited[num]:
            visited[num] = True
            state.append(num)
            bt()
            visited[num] = False
            state.pop()

bt()