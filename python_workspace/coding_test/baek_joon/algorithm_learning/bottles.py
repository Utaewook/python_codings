n,k = map(int, input().split())
print('count, L, q, r, answer')

if n <= k:
    print(0)
else:
    count = 0
    answer = 0
    while True:
        q, r = divmod(n, 2)
        if q + r <= k:
            break
        print(count, 2**count, q, r, answer)
        if r == 0:
            n = q
        else:
            n = q + 1
            answer += 2 ** count
        count += 1
        print(2**count)
        print(count, 2**count, q, r, answer,'\n')



    print(answer)
