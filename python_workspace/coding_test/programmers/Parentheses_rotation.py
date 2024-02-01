def solution(s):
    answer = 0
    for i in range(len(s)):
        if is_it_right(s[i:] + s[:i]):
            answer += 1
    return answer


def is_it_right(string):
    stack = []
    pair = {'{': '}', '[': ']', '(': ')'}
    for s in string:
        if not stack:
            stack.append(s)
            continue
        if stack[-1] in pair and pair[stack[-1]] == s:
            stack.pop()
        else:
            stack.append(s)
    return stack == []


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))