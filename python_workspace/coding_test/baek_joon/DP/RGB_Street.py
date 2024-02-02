N = int(input())

R, G, B = 0, 1, 2 # color index
input_costs = []
for _ in range(N):
    input_costs.append(list(map(int, input().split())))

s = 0
mem = list()
now = -1
for i in range(N):
    tempArray = list()
    if min(input_costs[i]) == input_costs[i][R]:
        if now == R and min(input_costs[i]) == input_costs[i][R]:
            tempArray = [input_costs[i][G], input_costs[i][B]]
            if min(tempArray) == tempArray[0]:
                now = G
            else:
                now = B
        else:
            now = R
    elif min(input_costs[i]) == input_costs[i][G]:
        if now == G and min(input_costs[i]) == input_costs[i][G]:
            tempArray = [input_costs[i][R], input_costs[i][B]]
            if min(tempArray) == tempArray[0]:
                now = R
            else:
                now = B
        else:
            now = G
    elif min(input_costs[i]) == input_costs[i][B]:
        if now == B and min(input_costs[i]) == input_costs[i][B]:
            tempArray = [input_costs[i][R], input_costs[i][G]]
            if min(tempArray) == tempArray[0]:
                now = R
            else:
                now = G
        else:
            now = B
    mem.append(now)

print(sum([input_costs[idx][mem[idx]] for idx in range(N)]))
# 최소값 찾지 못함 - dp 활용 할 것