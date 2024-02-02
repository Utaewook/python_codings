
N = int(input())

count = 0
dic = {}

dic[0] = 0
dic[1] = 1
dic[2] = 2

for i in range(3, N+1):
    dic[i] = (dic[i-1]+dic[i-2]) % 15746

print(dic[N])