def dfs(i, pw):
    global results
    if len(pw) == L:
        pw = list(pw)
        pw.sort()
        pw = ''.join(pw)
        results.add(pw)
        return

    for idx in range(i, C):
        dfs(idx + 1, pw + inputs[idx])


L, C = map(int, input().split())
inputs = list(input().split())
inputs.sort()

results = set()
dfs(0, '')
results = list(results)
results.sort()
for result in results:
    count = 0
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        if vowel in result:
            count += 1
    if count >= 1 and L - count >= 2:
        print(result)
