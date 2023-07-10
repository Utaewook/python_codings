T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    N, M = min(N, M), max(N, M)
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if len(A)>len(B):
        A,B = B,A
    max_val = 0
    for i in range(M-N+1):
        max_val = max(max_val,sum([A[j]*B[i+j] for j in range(N)]))
    print(f"#{test_case} {max_val}")
