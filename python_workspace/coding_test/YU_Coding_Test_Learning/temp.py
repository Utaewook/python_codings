def solution(s):
    answer = len(s)
    for length in range(1, len(s) // 2 + 1):
        compressed_string = ''
        stack = []
        print(f"length = {length}, s = {s}")
        for j in range(0, len(s), length):
            print(f"\tj = {j}, stack = {stack}, compressed_string = {compressed_string}")
            if j + length > len(s) + 1:
                compressed_string += s[j:]
                print("\t남은 문자열 짧아서 붙여서 끝냄")
                break

            if not stack:
                stack.append(s[j:j + length])
                print(f"\t스택 비어서 첫 단어 추가: {stack[0]}")
                continue
            else:
                curr_s = s[j:j + length]
                print(f"\t잘린 단어: curr_s = {curr_s}")
                if curr_s == stack[-1]:
                    stack.append(curr_s)
                    print(f"\t\t스택에 있는 거랑 같아서 스택에 추가했음: {stack}")
                    continue
                else:
                    if len(stack) == 1:
                        compressed_string += stack.pop()
                    else:
                        compressed_string += str(len(stack)) + stack.pop()
                    #print(f"\t\t스택에 있는거랑 달라서 스택에 있는거 압축해서 문자열 만듬: {compressed_string}")
                    stack = [curr_s]
        #print(f"스택에 남은거 있어서 남은거 붙이기 시작: {stack}")
        if len(stack) == 1:
            compressed_string += stack.pop()
        elif len(stack) >= 2:
            compressed_string += str(len(stack))+stack.pop()

        #print(f"남은거 붙이기 완료: {compressed_string}")
        answer = min(answer, len(compressed_string))
        #print(f"loop result: answer = {answer}, compressed_string = {compressed_string}\n")
    return answer


test_cases = ["aabbaccc",
              "ababcdcdababcdcd",
              "abcabcdede",
              "abcabcabcabcdededededede",
              "xababcdcdababcdcd"]

for test_case in test_cases:
    print(solution(test_case), end="\n\n\n")