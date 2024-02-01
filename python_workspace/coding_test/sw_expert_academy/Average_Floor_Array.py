T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    Q = int(input())
    query = list(map(int,input().split()))
    sum_val = sum(arr)
    query_max = max(query)
    while len(arr) < query_max:
        arr.append(int(sum_val/len(arr)))
        sum_val += arr[-1]
    print(f"#{test_case}",end=' ')
    for q in query:
        print(arr[q-1], end=' ')
    print()