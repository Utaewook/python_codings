T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    puzzle = [input() for _ in range(N)]
    answer = 0
    for p in puzzle:
        answer += p.replace(' ','').split('0').count('1'*K)
        p = list(p.split())
    t_puzzle = list(zip(*puzzle))
    for t_p in t_puzzle:
        answer += ''.join(t_p).split('0').count('1'*K)
    print(f"#{test_case} {answer}")