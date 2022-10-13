test_case = int(input())

def dfs():
    pass

result = []
for _ in range(test_case):
    n = int(input())
    arr = [0] + [*map(int,input().split())]
    visited = [False] * (n + 1)
