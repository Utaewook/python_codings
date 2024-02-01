import time

test_cases = [['a','b','c','d'],
              ['a','b','b','b','e'],
              ['a','b','c','d','b','q']]


def permutation(arr, n):
    result = set()

    def dfs(selected, rest):
        if len(selected) == n:
            result.add(''.join(selected))

        for i in range(len(rest)):
            selected.append(rest[i])
            dfs(selected,rest[:i]+rest[i+1:])
            selected.pop()

    dfs([], arr[:])
    return result


for test_case in test_cases:
    print(f'test_case = {test_case}')
    per = permutation(test_case,3)
    print(per)