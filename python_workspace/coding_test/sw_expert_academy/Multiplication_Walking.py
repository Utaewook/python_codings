T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    max_val = 1
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            max_val = max(max_val, i)
    if max_val == 1:
        print(f"#{test_case} {N+1}")
    else:
        print(f"#{test_case} {N//max_val+max_val - 2}")
