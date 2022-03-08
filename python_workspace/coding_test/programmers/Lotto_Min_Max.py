def solution(lottos, win_nums):
    answer = [0,0]
    zeros = len([x for x in lottos if x == 0])
    inter = len(set(lottos).intersection(set(win_nums)))
    inter_min,inter_max = inter,inter+zeros
    if zeros == 6:
        answer[0] = 1
        answer[1] = 6
    elif zeros == 0:
        answer[0] = 7 - inter_max
        answer[1] = 7 - inter_max
    elif inter_min < 2:
        answer[0] = 6
    elif inter_max < 2:
        answer[1] = 6
    else:
        answer[0] = 7 - inter_max
        answer[1] = 7 - inter_min
        
    return answer