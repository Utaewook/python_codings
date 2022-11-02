import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))


def is_cycle(x, prev):
    visited[x] = True
    for y in graph[x]:
        if visited[y]:
            if y != prev:
                return True
        else:
            if is_cycle(y, x):
                return False
    return False


# def result_print(tree_count):
#     results = ('No trees.', 'There is one tree.', f'A forest of {tree_count} trees.')
#     if tree_count > 1:
#         return results[2]
#     else:
#         return results[tree_count]


case_count = 0
while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    else:
        case_count += 1
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        count = 0

        for node in range(1, n + 1):
            if not visited[node]:
                if not is_cycle(node,0):
                    count += 1
        # print(f"Case {case_count}: " + result_print(count))

        if count == 0:
            print(f'Case {case_count}: No trees.')
        elif count == 1:
            print(f'Case {case_count}: There is one tree.')
        else:
            print(f'Case {case_count}: A forest of {count} trees.')




# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(int(1e6))
#
# def is_cycle(x,prev):
#     visited[x] = True
#     for y in graph[x]:
#         if visited[y]:
#             if y!=prev:
#                 return True
#         else:
#             if is_cycle(y,x):
#                 return True
#     return False
#
# test_case = 1
# while True:
#     n,m = map(int,input().split())
#     if n==0 and m==0:
#         break
#     graph = [[] for _ in range(n + 1)]
#     visited = [False]*(n+1)
#
#     for i in range(m):
#         x,y = map(int,input().split())
#         graph[x].append(y)
#         graph[y].append(x)
#
#     cnt = 0
#     for i in range(1,n+1):
#         if not visited[i]:
#             if not is_cycle(i,0):
#                 cnt+=1
#     if cnt == 0:
#         print(f'Case {test_case}: No trees.')
#     elif cnt == 1:
#         print(f'Case {test_case}: There is one tree.')
#     else:
#         print(f'Case {test_case}: A forest of {cnt} trees.')
#     test_case += 1
