import sys
input = sys.stdin.readline

# Union-find 알고리즘을 통해 해결
# 점을 정점, 턴마다 긋는 선분을 간선으로 하는 그래프를 그려나가면서
# 사이클인지 판별하는 것으로 구현한다.

# x 라는 점의 부모 노드를 찾는다(루트) = 재귀적으로 호출

# 작은 노드를 부모 노드로 하는 트리를 그리다가, 루트 노드를 찾는 함수인 find_parent()에 간선의 각 노드를 넣었을때 같은
# 루트 노드가 반환 된다면 사이클이 되는 원리

# 만약 입력된 간선의 두 노드의 루트 노드가 다르다면 간선으로 연결해 줘서 루트노드에 포함시킨다

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


dot, turns = map(int, input().split())
parent = [i for i in range(dot)]

cycle = False
for i in range(turns):
    print(parent)
    a, b = map(int,input().split())
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        print(i+1)
        break
    else:
        union_parent(parent,a,b)

if not cycle:
    print(0)


