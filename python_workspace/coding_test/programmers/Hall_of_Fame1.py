def solution(k, score):
    answer = []
    l = list()
    for s in score:
        l.append(s)
        l.sort(reverse=True)
        if len(l) < k:
            answer.append(l[-1])
        else:
            answer.append(l[k-1])

    return answer