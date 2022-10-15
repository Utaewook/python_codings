def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] else -absolutes[i] for i in range(len(absolutes))])


test_case = (([4,7,12],[True,False,True]),([1,2,3],[False,False,True]))

for test in test_case:
    print(solution(test[0],test[1]))