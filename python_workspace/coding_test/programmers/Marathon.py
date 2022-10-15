import collections


def solution(participant, completion):
    participant = collections.Counter(participant)
    completion = collections.Counter(completion)

    if participant.keys() == completion.keys():
        pass




test_case=(["leo", "kiki", "eden"],["eden", "kiki"])
print(solution(test_case[0],test_case[1]))