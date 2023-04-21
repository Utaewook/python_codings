import math

def solution(brown,yellow):
    return [int(((brown+4)+math.sqrt((brown+4)**2-16*(brown+yellow)))//4),int(((brown+4)-math.sqrt((brown+4)**2-16*(brown+yellow)))//4)]


print(solution(10,2))
print(solution(8,1))
print(solution(24,24))
