import sys
input = sys.stdin.readline

n, m = map(int,input().split())

dic = dict()
for i in range(1, n+1):
    name = input().rstrip()
    dic[str(i)] = name
    dic[name] = str(i)

for _ in range(m):
    print(dic[input().rstrip()])