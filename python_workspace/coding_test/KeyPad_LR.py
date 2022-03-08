def solution(numbers, hand):
    answer = ''
    L,R = -1
    for i in range(len(numbers)):
        if numbers[i] in [2,5,8,0]:
            if L+2==R:# 위치가 같은 경우
                answer += hand[0].upper()
                
        elif numbers[i] in [1,4,7]:
            answer += 'L'
            L = numbers[i]
        elif numbers[i] in [3,6,9]:
            answer += 'R'
            R = numbers[i]
        
    return answer
