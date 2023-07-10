def solution(food):
    answer = ''
    for i in range(1,len(food)):
        f = food[i]
        answer += str(i)*(f//2)
    return answer + '0' + ''.join(reversed(list(answer)))


print(solution([1,3,4,6]))