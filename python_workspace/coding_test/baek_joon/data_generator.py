import random

# row,col = map(int,input().split())
# f = open('outputs.txt','w')
# for i in range(row):
#     for j in range(col):
#         data =f'{random.randrange(1,10)} '
#         f.write(data)
#     f.write('\n')
#
# f.close()


n = int(input())
f = open('outputs.txt','w')

f.write(f'{n}\n')
for i in range(n):
    data = f'{random.randrange(1,50000)} '
    f.write(data)
f.close()
