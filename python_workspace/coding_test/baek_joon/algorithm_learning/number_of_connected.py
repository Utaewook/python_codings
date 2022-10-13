import sys
input = sys.stdin.readline

 #
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int,input().split())

parent = [x for x in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent,a,b)

counter = set()
for i in range(1,n+1):
    counter.add(find_parent(parent, i))

print(len(counter))