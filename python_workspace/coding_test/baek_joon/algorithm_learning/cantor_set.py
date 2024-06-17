
def cantor(n):
    if n in memo:
        return memo[n]

    else:
        pre = cantor(n-1)
        res = pre + ' '*(3**(n-1)) + pre
        memo[n] = res
        return res

memo = {0: '-', 1:'- -'}
while True:
    try:
        n = int(input())
    except:
        break

    print(cantor(n))
