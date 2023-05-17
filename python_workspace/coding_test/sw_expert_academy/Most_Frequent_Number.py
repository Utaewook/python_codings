# import sys
# input = sys.stdin.readline


test_cases = int(input())

for _ in range(test_cases):
    test_case = int(input())
    count = [0 for _ in range(101)]
    scores = list(map(int,input().split()))
    for s in scores:
        count[s] += 1
    max_val = max(count)
    for i in range(100,-1,-1):
        if count[i] == max_val:
            print(f"#{test_case} {i}")
            break
