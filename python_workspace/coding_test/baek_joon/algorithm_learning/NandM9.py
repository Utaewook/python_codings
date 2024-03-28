n, m = map(int,input().split())

nums = sorted(list(map(int,input().split())))

count = {}

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
        printed.add(output)
        print(output)
        return

    for num in nums:
        if count[num]:
            state.append(num)
            count[num] -= 1
            bt()
            state.pop()
            count[num] += 1

bt()
