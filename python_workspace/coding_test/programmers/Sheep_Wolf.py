def solution(info, edges):
    answer = 0
    tree = dict()
    for parent, child in edges:
        if parent in tree:
            tree[parent].append(child)
        else:
            tree[parent] = [child]

        if child in tree:
            tree[child].append(parent)
        else:
            tree[child] = [parent]

    print(tree)

    def dfs(node, sheep, wolf, path):
        nonlocal answer
        if info[node] == 0:
            sheep += 1
        elif info[node] == 1:
            wolf += 1
        else:
            return

        info[node] = -1

        if wolf >= sheep:
            return

        answer = max(answer, sheep)

        for next_node in tree[node]:
            path.append(next_node)
            dfs(next_node, sheep, wolf, path)
            print(path, next_node)
            path.pop()

    dfs(0, 0, 0, [0])

    return answer


test_cases = [[[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]], 5],
              [[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]], 5]]

for test_case in test_cases:
    result = solution(test_case[0], test_case[1])
    print(f"answer is {test_case[2]}, result is {result}")
