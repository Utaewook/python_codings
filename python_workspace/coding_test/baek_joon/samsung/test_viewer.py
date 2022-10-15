
n = int(input()) # 시험장의 갯수
a = list(map(int,input().split())) # 각 시험장에 있는 응시자의 수
b,c = map(int,input().split())

for i in range(len(a)):
    a[i] -= b
    if a[i] < 0:
        a[i] = 0
    if a[i] % c == 0:
        a[i] = 1 + a[i]//c
    else:
        a[i] = 1 + a[i]//c + 1

print(sum(a))