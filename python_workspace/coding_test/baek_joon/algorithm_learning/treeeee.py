n = int(input())
tree_parents = list(map(int, input().split()))
del_node = int(input())


def is_leaf(node):
    if node not in tree_parents: # 각 노드의 부모 리스트에 해당 노드가 포함 되어 있지 않다면
        return True  # 리프 노드이다
    else: # 그외엔
        return False  # 부모 노드이다.