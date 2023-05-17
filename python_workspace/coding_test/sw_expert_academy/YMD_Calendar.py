T = int(input())

day_limit = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for test_case in range(1,T+1):
    ymd = input()
    yyyy,mm,dd = ymd[:4],ymd[4:6],ymd[6:]
    if day_limit[int(mm)]<int(dd):
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {yyyy}/{mm}/{dd}')

