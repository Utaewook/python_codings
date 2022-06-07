N = int(input())

test_cases = []

for _ in range(N):
    test_cases.append(int(input()) - 1)

dic = {}
dic[0] = dic[1] = dic[2] = 1

def padovan_seq(n):
    if n not in dic.keys():
        dic[n] = padovan_seq(n - 2)+padovan_seq(n - 3)
    return dic[n]

for test_case in test_cases:
    print(padovan_seq(test_case))