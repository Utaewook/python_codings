n = int(input())
input_array = list(map(int,input().split()))

mem = list()
now = 0
if max(input_array) <= 0:
    print(max(input_array))
else:
    for num in input_array:
        if now + num <= 0:
            now = 0
            continue
        now += num
        mem.append(now)
    print(max(mem))
