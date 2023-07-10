def solution(s):
    s = s[1:-1]
    tuples = []
    stack = ''
    answer = []
    for c in s:
        if c == '{':
            stack = ''
            continue
        elif c == '}':
            tuples.append(list(map(int,stack.split(','))))
            stack = ''
        else:
            stack += c
    tuples.sort(key=lambda x : len(x),reverse=True)
    while tuples:
        t = tuples.pop()
        for n in t:
            if n not in answer:
                answer.append(n)
                break
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))