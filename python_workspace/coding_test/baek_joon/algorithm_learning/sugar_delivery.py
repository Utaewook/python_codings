n = int(input())
min_val = n

for i3 in range(n//3 + 1):
    i5 = (n - (3 * i3)) // 5
    if i3*3 + i5*5 == n:
        min_val = min(min_val, i3+i5)

if min_val == n:
    print(-1)
else:
    print(min_val)