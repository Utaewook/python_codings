n = int(input())
tree_parents = list(map(int, input().split()))
del_node = int(input())

def is_leaf(node):
    if tree_parents[node] is None:  # node가 삭제된 노드이면
        return False  # 리프 노드가 아님
    else:  # node가 삭제되지 않은 노드이며,
        if node not in tree_parents: # 각 노드의 부모 리스트에 해당 노드가 포함 되어 있지 않다면
            return True  # 리프 노드이다
        else: # 그외엔
            return False  # 부모 노드이다.

def del_n(node_num):
    tree_parents[node_num] = None
    if node_num in tree_parents:
        i = tree_parents.index(node_num)
        tree_parents[i] = None
        del_n(node_num)
        del_n(i)
    else:
        return

del_n(del_node)
count = 0
for no in range(n):
    if is_leaf(no):
        count += 1

print(count)