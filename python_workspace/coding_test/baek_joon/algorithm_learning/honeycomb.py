n = int(input())

count = 1
n-=1

while n > 0:
    n -= 6*count
    count += 1

print(count)