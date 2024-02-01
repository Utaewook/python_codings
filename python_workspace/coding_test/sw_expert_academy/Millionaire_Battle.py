# def solution(bakery_schedule, current_time, k):
#     curr_hour, curr_minute = map(int,current_time.split(':'))
#     bread_sum = 0
#     for i in range(len(bakery_schedule)):
#         t, bread = bakery_schedule[i].split()
#         bread = int(bread)
#         hour, minute = map(int,t.split(':'))
#         if hour < curr_hour or (hour == curr_hour and minute < curr_minute):
#             continue
#         bread_sum += bread
#         if bread_sum >= k:
#             return abs(curr_hour-hour)*60 + abs(curr_minute-minute)
#     return -1
#
# s = set()
#
# def solution(p, b):
#     answer = []
#     tree = {}
#
#     for i in range(len(p)):
#         if p[i] == -1:
#             continue
#         elif p[i] not in tree:
#             tree[p[i]] = [i]
#         else:
#             tree[p[i]].append(i)
#
#     for id in b:
#         if p[id] == -1:
#             global s
#             s.add(id)
#             count(tree, id)
#             answer.append(len(s))
#             s = set()
#         else:
#             answer.append(0)
#
#     return answer
#
# def count(t, curr_id):
#     if curr_id not in t:
#         return
#     global s
#     for i in t[curr_id]:
#         s.add(i)
#         count(t, i)
#
# print(solution([2, 2, -1, 1, 5, -1, 5], [2, 5]))
# print(solution([2, 2, -1, 1, 5, -1, 5], [1, 5]))


def solution(boards):
    answer = []
    for board in boards:
        print()
        m = []
        for i in range(len(board)):
            m.append(list(map(int, list(board[i]))))
        print(m)

        curr_r, curr_c = -1, -1
        for i in range(len(m)):
            for j in range(len(m)):
                if m[i][j] == 2:
                    curr_r, curr_c = i, j
                    break
            if curr_r != -1 or curr_c != -1:
                break

        m[curr_r][curr_c] = 1
        dfs(m, curr_r, curr_c)
        print(m)
        m = sum(m,[])
        print(m)
        if 1 in m:
            answer.append(0)
        else:
            answer.append(1)

    return answer


def dfs(maze,r,c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    maze[r][c] = 3  # 3은 꽃을 의미

    for d in range(4):
        curr_r = r + dr[d]
        curr_c = c + dc[d]
        if curr_r in [-1,len(maze)] or curr_c in [-1,len(maze)]: # 다음 칸이 지도 밖인경우
            continue

        if maze[curr_r][curr_c] == 1:
            dfs(maze,curr_r,curr_c)
            break
    return

print(solution([["00011", "01111", "21001", "11001", "01111"], ["00011", "00011", "11111", "12101", "11111"]]))
print(solution([["1111", "1121", "1001", "1111"], ["0000", "0000", "0000", "0002"], ["0000", "0100", "0000", "0002"], ["0000", "0010", "0121", "0010"]]))