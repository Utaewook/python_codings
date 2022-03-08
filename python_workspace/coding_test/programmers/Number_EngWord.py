
def solution(s):
    dic = ("zero","one","two","three","four","five","six","seven","eight","nine")
    answer = ''
    if s.isdigit():
        return int(s)
    
    i = 0
    while i < len(s):
        if s[i:i+3] in dic:
            answer += str(dic.index(s[i:i+3]))
            i+=3
        elif s[i:i+4] in dic:
            answer += str(dic.index(s[i:i+4]))
            i+=4
        elif s[i:i+5] in dic:
            answer += str(dic.index(s[i:i+5]))
            i+=5
        elif s[i].isdecimal():
            answer += str(s[i])
            i+=1
            
    return int(answer)

# test_case = ("one4seveneight","23four5six7","2three45sixseven","123")
# for idx in range(len(test_case)):
#     print(solution(test_case[idx]))
    
# 다른 사람의 풀이

# replace 함수 사용
# def solution(s):
#     words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

#     for i in range(len(words)):
#         s = s.replace(words[i], str(i))

#     return int(s)