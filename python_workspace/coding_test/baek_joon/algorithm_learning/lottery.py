state = list()

def bt():
    if len(state) == 6:
        print(' '.join(map(str, state)))
        return
    for num in nums:
        if state and state[-1] >= num:
            continue
        if not visited[num]:
            state.append(num)
            visited[num] = True
            bt()
            state.pop()
            visited[num] = False


while True:
    line = input()
    if line == '0':
        break

    line = list(map(int, line.split()))
    k, nums = line[0], line[1:]
    visited = {num: False for num in nums}

    bt()

    print()


