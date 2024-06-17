def concat_hor(arr1, arr2):
    res = list()
    for l1, l2 in zip(arr1, arr2):
        res.append(l1 + l2)

    return res


def func(i):
    if i not in memo:
        pre = func(i//3)
        updown = concat_hor(concat_hor(pre, pre), pre)
        mid = concat_hor(concat_hor(pre, [[' ' for _ in range(i//3)] for _ in range(i//3)]), pre)

        result = updown + mid + updown
        memo[i] = result

    return memo[i]


memo = {3: [['*', '*', '*'],
            ['*', ' ', '*'],
            ['*', '*', '*']]}
n = int(input())

s = func(n)

for l in s:
    for c in l:
        print(c,end='')
    print()