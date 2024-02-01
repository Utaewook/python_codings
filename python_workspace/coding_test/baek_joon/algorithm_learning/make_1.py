num = int(input())

mem = {0:set()}
mem[0].add(num)

def dp(n):
    if n not in mem:
        temp = set()
        for x in dp(n - 1):
            if x % 3 == 0:
                temp.add(x // 3)
            if x % 2 == 0:
                temp.add(x // 2)
            temp.add(x - 1)
        mem[n] = temp
    return mem[n]

idx = 0
while True:
    s = dp(idx)
    if 1 in s:
        break
    idx+=1
print(idx)

