n, m = map(int, input().split())

nums = sorted(list(map(int,input().split())))

state = []

printed = set()
def bt():
    if len(state) == m:
        output = ' '.join(map(str, state))
        if output in printed:
            return
        printed.add(output)
        print(output)
        return
    for num in nums:
        if state and state[-1] > num:
            continue
        state.append(num)
        bt()
        state.pop()

bt()