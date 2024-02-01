import math

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    val = 0
    for x in range(N):
        val += int(math.sqrt(N**2-x**2))
    print(f"#{test_case} {4*val+1}")