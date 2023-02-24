arr = [0]
n = int(input())
visited = [False] * (n + 1)
finished = [False] * (n + 1)
for _ in range(n):
    arr.append(int(input()))

answer = []


def is_cycle(num):
    visited[num] = True
    nn = arr[num]
    if not visited[nn]:
        is_cycle(nn)
    elif not finished[nn]:
        while nn != num:
            answer.append(nn)
            nn = arr[nn]
        answer.append(num)
    finished[num] = True

for x in range(1, n + 1):
    if not visited[x]:
        is_cycle(x)

answer.sort()
print(len(answer))
for a in answer:
    print(a)
