import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

test_case = int(input())


# 그래프의 사이클의 판별은 두개의 리스트를 통해 방문 여부와 처리 완료 데이터를 갱신하며 판별한다
def is_cycle(x):
    visited[x] = True
    y = arr[x]  # 다음 노드

    if not visited[y]:
        is_cycle(y)
    elif not finished[y]:  # 사이클 발생
        while y != x:
            result.append(y)
            y = arr[y]
        result.append(x)
    finished[x] = True


for _ in range(test_case):
    result = []
    n = int(input())
    arr = [0] + [*map(int, input().split())]
    visited = [False] * (n + 1)
    finished = [False] * (n + 1)

    for x in range(1, n + 1):
        if not visited[x]:
            is_cycle(x)

    print(n - len(result))
