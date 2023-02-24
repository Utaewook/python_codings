import random

row,col = map(int,input().split())
f = open('outputs.txt','w')
for i in range(row):
    for j in range(col):
        data =f'{random.randrange(1,10)} '
        f.write(data)
    f.write('\n')

f.close()
