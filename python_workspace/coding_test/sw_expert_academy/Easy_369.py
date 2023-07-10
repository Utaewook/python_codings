N = int(input())

for i in range(1,N+1):
    val = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if val == 0:
        print(i, end=' ')
    else:
        print('-'*val, end=' ')
