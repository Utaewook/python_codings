
# def fibo(n):
#     global count0
#     global count1
#     if n == 0:
#         count0 += 1
#         return 0
#     elif n == 1:
#         count1 += 1
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)

dic = {}

def init():
    global dic

    dic.clear()
    dic[0] = 0
    dic[1] = 1

def fibo_dp(n):
    if n not in dic.keys():
        dic[n] = fibo_dp(n-1) + fibo_dp(n-2)
    return dic[n]

N = int(input())

test_case = []
for _ in range(N):
    test_case.append(int(input()))

for n in test_case:
    if n == 0:
        print(1,0)
    elif n==1:
        print(0,1)
    else:
        init()
        fibo_dp(n)
        print(f"{dic[n-1]} {dic[n]}")
