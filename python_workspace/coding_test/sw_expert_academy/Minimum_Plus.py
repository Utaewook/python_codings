T = int(input())

for test_case in range(1, T+1):
    ab = input()
    min_val = int(ab)
    for i in range(1,len(ab)):
        min_val = min(min_val,int(ab[:i])+int(ab[i:]))
    print(f'#{test_case} {min_val}')