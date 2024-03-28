n, m = map(int,input().split())

nums = sorted(list(map(int,input().split())))

count = dict()

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

state = []
printed = set()

def bt():
    if len(state) == m:
        output = ' '.join(map(str, state))

        if output in printed:
            return

        print(output)
        printed.add(output)
        return

    for num in nums:
        if state and state[-1] > num:
            continue

        if count[num]:
            state.append(num)
            count[num] -= 1
            bt()
            state.pop()
            count[num] += 1

bt()