n = 1000-int(input())

count = 0
while n:
    if n >= 500:
        n -= 500
    elif 100 <= n < 500:
        n -= 100
    elif 50 <= n < 100:
        n -= 50
    elif 10 <= n < 50:
        n -= 10
    elif 5 <= n < 10:
        n -= 5
    elif 1 <= n < 5:
        n -= 1
    count += 1
print(count)
