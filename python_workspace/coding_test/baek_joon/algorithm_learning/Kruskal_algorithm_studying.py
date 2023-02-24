mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'), (5, 'A', 'D'), (9, 'D', 'B'), (8, 'B', 'C'), (5, 'C', 'E'), (7, 'D', 'E'), (6, 'D', 'F'),
        (8, 'F', 'E'), (11, 'F', 'G'), (9, 'E', 'G'), (7, 'B', 'E'), (7, 'B', 'A'), (5, 'D', 'A'), (9, 'B', 'D'),
        (8, 'C', 'B'), (5, 'E', 'C'), (7, 'E', 'D'), (6, 'F', 'D'), (8, 'E', 'F'), (11, 'G', 'F'), (9, 'G', 'E'),
        (7, 'E', 'B')
    ]
}

parent = dict()
rank = dict()


def make_set(node):
    parent[node] = node
    rank[node] = 0


def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v,node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def kruskal(graph):
    mst = list()

    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 사이클 없는 간선만 연결
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u): # 사이클이 없는 경우
            union(node_v,node_u)
            mst.append(edge)

    return mst


print(kruskal(mygraph))