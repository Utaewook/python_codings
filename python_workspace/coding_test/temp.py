def combinations(arr, r):
    n = len(arr)
    result = []
    count = 0

    def dfs(idx):
        nonlocal count

        if count == r:
            print(result)
            return

        if idx == n:
            return

        # 현재 원소 선택
        result.append(arr[idx])
        count += 1
        dfs(idx + 1)

        # 현재 원소 선택 안 함
        result.pop()
        count -= 1
        dfs(idx + 1)

    dfs(0)



combinations([i for i in range(6)],2)