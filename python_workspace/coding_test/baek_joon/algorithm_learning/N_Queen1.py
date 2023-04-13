# N = int(input())
#
# def is_able(r, c, candidate):
#     attackable_locations = []
#     for candidate_row in range(len(candidate) + 1, N):
#         for candidate_col in range(N):
#             if r == candidate_row or c == candidate_col or abs((c-candidate_col)/(r-candidate_row)) == 1:
#                 attackable_locations.append((candidate_row,candidate_col))
#
#     if (r, c) not in attackable_locations:
#         return True
#     return False
#
#
# def dfs(col, current_candidates):
#     row = len(current_candidates)
#
#     for i in range(N):
#         if is_able(row,col,current_candidates):
#             current_candidates.append((row,col))
#             dfs(col+i,current_candidates)
#             current_candidates.remove((row,col))
#             if
#         else:
#             return
#
#
#
#
# def solve_n_queen(N):
#     dfs(0, [])
#
#
# solve_n_queen(N)
#
# print(1==1.0)

# x번째 행에 놓은 퀸에 대해 검증
def check(x):
    for i in range(x): # 이전 행에서 놓았던 모든 퀸들을 확인
        if row[x] == row[i]:  # 위쪽 확인
            return False
        if abs(row[x]-row[i]) == x-i:  # 대각선 확인
            return False
    return True

def dfs(x):  # x번째 행에 대하여 처리
    global result
    if x == N:
        result += 1
    else:   # x 번쨰 행의 각 열에 퀸을 둔다고 가정
        for i in range(N):
            row[x]=i
            if check(x):
                dfs(x+1)  # 다음행으로

N = int(input())
row = [0]*N
result = 0
dfs(0)
print(result)