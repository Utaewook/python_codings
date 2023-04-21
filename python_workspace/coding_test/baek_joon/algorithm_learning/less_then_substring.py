def solution(t, p):
    answer = 0
    int_p = int(p)
    for i in range(len(t) - len(p)+1):
        if int(t[i:i+len(p)]) <= int_p:
            answer += 1

    return answer


print(solution("3141592", "271"))
print()
print(solution("500220839878", "7"))
print()
print(solution("10203", "15"))