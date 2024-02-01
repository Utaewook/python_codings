def solution(N, number):
    if N == number:
        return 1
    elif int(len(str(number))*str(N)) == number:
        return len(str(number))
    answer = 9
    mem = {1:[N],
           2:[N*11,N+N,N//N,N-N,N*N]}

    def dp(n):
        nonlocal answer
        if n not in mem:
            temp = set()
            temp.add(N*int('1'*n))
            for i in range(1, n):
                array_1, array_2 = dp(i), dp(n-i)
                for a in array_1:
                    for b in array_2:
                        temp.add(a+b)
                        temp.add(a*b)
                        if b != 0:
                            temp.add(a//b)
                        if a-b > 0:
                            temp.add(a-b)
            mem[n] = list(temp)
            if number in temp:
                answer = min(answer,n)

        return mem[n]

    dp(9)

    return answer if answer < 9 else -1