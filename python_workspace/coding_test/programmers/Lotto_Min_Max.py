def solution(lottos, win_nums):
    answer = [0, 0]
    zeros = len([x for x in lottos if x == 0])
    inter = len(set(lottos).intersection(set(win_nums)))
    inter_min, inter_max = inter, inter + zeros
    if zeros == 0:
        if inter == 0:
            answer = [6, 6]
        elif inter == 6:
            answer = [1, 1]
        else:
            answer = [7 - inter_max, 7 - inter_min]
    elif zeros == 6:
        answer = [1, 6]
    else:
        if inter == 0:
            answer = [7 - zeros, 6]
        else:
            answer = [7 - inter_max, 7 - inter_min]

    return answer


# 다른 사람의 풀이

# def solution(lottos, win_nums):
#
#     rank=[6,6,5,4,3,2,1]
#
#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]

# def solution(lottos, win_nums):
#     rank = {
#         0: 6,
#         1: 6,
#         2: 5,
#         3: 4,
#         4: 3,
#         5: 2,
#         6: 1
#     }
#     return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]