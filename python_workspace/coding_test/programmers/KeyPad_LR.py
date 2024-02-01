
def solution(numbers, hand):
    keyPad = [[1,2,3],
              [4,5,6],
              [7,8,9],
              [10,11,12]]
    answer = ''
    hand = hand[0].upper()
    L_position = 10
    R_position = 12
    for number in numbers:
        if number == 0:
            number = 11
        if number in [i[0] for i in keyPad]:
            answer += 'L'
            L_position = number
        elif number in [i[2] for i in keyPad]:
            answer += 'R'
            R_position = number
        else:
            L_distance = abs((L_position-1)//3 - (number-1)//3)+abs((L_position-1)%3 - (number-1)%3)
            R_distance = abs((R_position-1)//3 - (number-1)//3)+abs((R_position-1)%3 - (number-1)%3)
            if L_distance < R_distance:
                answer += 'L'
                L_position = number
            elif L_distance > R_distance:
                answer += 'R'
                R_position = number
            else:
                answer += hand
                if hand == 'L' : L_position = number
                else : R_position = number

    return answer

test_cases = (([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right'),([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],'left'),([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],'right'))

for test_case in test_cases:
    print(test_case)
    print(solution(test_case[0],test_case[1]))