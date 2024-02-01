def dfs(x):
    visited[x] = True
    for y in graph[x]:  # next vertex
        if len(s1) == 0 and len(s2) == 0:
            if x != y:
                s1.add(x)
                s2.add(y)
            else:
                s1.add(x)
                return
        if not visited[y]:
            if x in s1 and y not in s2:
                s2.add(y)
            elif x in s2 and y not in s1:
                s1.add(y)
            dfs(y)

def is_bipartite():
    for x in s1:
        if len(set(graph[x]).intersection(s1)) != 0:
            return False
    for x in s2:
        if len(set(graph[x]).intersection(s2)) != 0:
            return False
    return True


if __name__ == "__main__":
    test_case = int(input())

    for _ in range(test_case):
        v, e = map(int, input().split())
        graph = [[]for _ in range(v + 1)]
        visited = [False] * (v + 1)
        s1 = set()
        s2 = set()
        for _ in range(e):
            v1, v2 = map(int, input().split())
            graph[v1].append(v2)
            graph[v2].append(v1)

        for i in range(1, v + 1):
            if not visited[i]:
                dfs(i)
        if is_bipartite():
            print("YES")
        else:
            print("NO")
