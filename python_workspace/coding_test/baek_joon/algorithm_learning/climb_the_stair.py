N = int(input())
step = [0]*(N+1)
a = [0]*(N+1)

for i in range(1,N+1):
    step[i] = int(input())
if N == 1:
    print(step[1])
elif N == 2:
    print(sum(step))
else:
    a[1] = step[1]
    a[2] = step[1]+step[2]
    a[3] = max(step[1]+step[3],step[2]+step[3])
    for i in range(4,N+1):
        a[i] = max(a[i-2]+step[i], a[i-3]+step[i]+step[i-1])
    print(a[N])