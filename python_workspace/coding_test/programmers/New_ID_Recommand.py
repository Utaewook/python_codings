def solution(new_id):
    answer = ''
    answer = new_id.lower() # 1단계
    i = 0
    while i < len(answer): # 2단계
        if answer[i] not in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
            answer = answer.replace(answer[i],"")
        else:
            i+=1
    
    i = 0        
    while i < len(answer)-1:
        if answer[i]+answer[i+1] == "..":
            answer = answer.replace('..','.')
        else:
            i+=1
    answer = answer.strip('.') # 3,4 단계
    
    if len(answer) == 0: # 5단계
        answer = 'a'
    elif len(answer) >= 16:
        answer = answer[0:15].strip('.')
        
    if len(answer) <= 2:
        while len(answer)<3:
            answer = answer+answer[len(answer)-1]
        
    return answer


# 다른 사람의 풀이

# 정규식 사용한 풀이

# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st

# 정규식 사용하지 않은 풀이

# def solution(new_id):
#     answer = ''
#     # 1
#     new_id = new_id.lower()
#     # 2
#     for c in new_id:
#         if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
#             answer += c
#     # 3
#     while '..' in answer:
#         answer = answer.replace('..', '.')
#     # 4
#     if answer[0] == '.':
#         answer = answer[1:] if len(answer) > 1 else '.'
#     if answer[-1] == '.':
#         answer = answer[:-1]
#     # 5
#     if answer == '':
#         answer = 'a'
#     # 6
#     if len(answer) > 15:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]
#     # 7
#     while len(answer) < 3:
#         answer += answer[-1]
#     return answer