n = int(input())
top = list(map(int, input().split()))
stack = []
answer = [0 for i in range(n)]

for i in range(n):  # 0부터 n까지 반복 -> top에 접근, answer에 정답 넣기
    print(top[i],stack)
    while stack:  # stack이 남아있는 동안
        if stack[-1][1] > top[i]:  # stack에 마지막 값이 현재 i위치의 탑의 높이보다 크다면
            answer[i] = stack[-1][0] + 1  # 정답에 stack의 마지막 값의 인덱스+1 값을 넣는다
            break # while 반복문 종료
        else:  # stack마지막 값이 현재 i 위치의 탑의 높이보다 작거나 같은 경우
            stack.pop()   # stack에 값을 뱬다
    stack.append([i, top[i]]) # stack에 i 인덱스와 i번째 탑의 높이를 append

print(*answer)
