# 삼성 코딩 테스트 - 퇴사

N = int(input())
schedule = []
for i in range(N):
    temp = list(map(int,input().split()))
    if temp[0] + i <= N:
        schedule.append(temp)
    else:
        schedule.append(False)

schedule_Stack = []

for i in range(N - 1, -1, -1):
    if schedule[i]:
        if len(schedule_Stack) == 0 or schedule[i][0] - 1 < schedule_Stack[len(schedule_Stack)-1] - i:
            schedule_Stack.append(i)
        else:
            s = 0
            for x in list(reversed(schedule_Stack)):
                if i+schedule[i][0]-1 < x: break
                s += schedule[x][1]
            if schedule[i][1] > s:
                for idx in range(len(schedule_Stack)-1, 0, -1):
                    if i+schedule[i][0]-1 >= schedule_Stack[idx]:
                        schedule_Stack = schedule_Stack[0:idx+1]
                        schedule_Stack.append(i)

ss = 0
for i in schedule_Stack:
    ss += schedule[i][1]
print(ss)