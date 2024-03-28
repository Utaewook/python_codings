n, m = map(int, input().split())

nums = sorted(list(map(int,input().split())))

state = []

def bt():
    if len(state) == m:
        print(' '.join(map(str, state)))
        return
    for num in nums:
        state.append(num)
        bt()
        state.pop()

bt()