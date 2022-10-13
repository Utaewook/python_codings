# # 삼성 코딩 테스트 - 퇴사
#
# N = int(input())
# schedule = []
# for i in range(N):
#     temp = list(map(int,input().split()))
#     if temp[0] + i <= N:
#         schedule.append(temp)
#     else:
#         schedule.append(False)
#
# schedule_Stack = []
#
# for i in range(N - 1, -1, -1):
#     if schedule[i]:
#         if len(schedule_Stack) == 0 or schedule[i][0] - 1 < schedule_Stack[len(schedule_Stack)-1] - i:
#             schedule_Stack.append(i)
#         else:
#             s = 0
#             for x in list(reversed(schedule_Stack)):
#                 if i+schedule[i][0]-1 < x: break
#                 s += schedule[x][1]
#             if schedule[i][1] > s:
#                 for idx in range(len(schedule_Stack)-1, 0, -1):
#                     if i+schedule[i][0]-1 >= schedule_Stack[idx]:
#                         schedule_Stack = schedule_Stack[0:idx+1]
#                         schedule_Stack.append(i)
#
# ss = 0
# for i in schedule_Stack:
#     ss += schedule[i][1]
# print(ss)

# N = int(input())
# schedule = []
#
# for n in range(N):
#     schedule.append(tuple(map(int, input().split())))
#
# counsel_queue = []
#
# def func(day):
#     print(counsel_queue)
#     if day < 0:
#         return sum([schedule[x][1] for x in counsel_queue])
#     elif day + schedule[day][0] > N:
#         return func(day-1)
#     elif len(counsel_queue) == 0 or schedule[day][0] == 1:
#         counsel_queue.append(day)
#         return func(day-1)
#     else:
#         if day+schedule[day][0] < counsel_queue[0]:
#             if sum([schedule[x][1] if day <= x < day+schedule[day][0] else 0 for x in counsel_queue]) < schedule[day][1]:
#                 for idx in counsel_queue:
#                     if idx < day+schedule[day][0]:
#                         counsel_queue.remove(idx)
#                 counsel_queue.append(day)
#         else:
#             if sum([schedule[x][1] if day <= x < day+schedule[day][0] else 0 for x in counsel_queue]) < schedule[day][1]:
#                 for idx in counsel_queue:
#                     if idx < day+schedule[day][0]:
#                         counsel_queue.remove(idx)
#                 counsel_queue.append(day)
#             elif sum([schedule[x][1] for x in counsel_queue]) < schedule[day][1]:
#                 counsel_queue.clear()
#                 counsel_queue.append(day)
#             else:
#                 counsel_queue.append(day)
#         return func(day-1)
#
# print(func(N-1))

N = int(input())
schedule = [list(map(int, input().rstrip().split())) for _ in range(N)]

counsel_queue = [0]*30

for i in range(N):
    a = max(schedule[i][1],counsel_queue[i+schedule[i][0]+1])
    for t in range(i+schedule[i][0]+1,N+2):
        counsel_queue[t] = max(a,counsel_queue[t])
    else:
        a = max(max(counsel_queue[:i+2])+schedule[i][1],counsel_queue[i+schedule[i][0]+1])
        for t in range(i+schedule[i][0]+1,N+2):
            counsel_queue[t] = max(a,counsel_queue[t])

print(max(counsel_queue[:N+2]))

sum = 0
sequence = [1,1,1]

for i in range(N - 1,-1,-1):
    if schedule[i][0] + i > N:
        continue
    else:
        pass
