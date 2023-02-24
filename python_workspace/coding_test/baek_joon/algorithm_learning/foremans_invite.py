tree = int(input())
trees = [*map(int, input().split())]
trees.sort()

m = 0
for day in range(tree):
    m = max(m, trees.pop()-(tree-day-1))

print(m+tree+1)