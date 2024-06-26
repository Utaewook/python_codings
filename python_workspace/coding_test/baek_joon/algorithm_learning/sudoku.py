def num_able(num, pool):
    if num in pool:
        return False
    return True


prob = [list(map(int,input().split())) for _ in range(9)]
blanks = set()

for i in range(9):
    for j in range(9):
        if prob[i][j] == 0:
            blanks.add((i,j))

