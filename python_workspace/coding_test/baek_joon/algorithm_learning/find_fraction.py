n = int(input())

count = 1

while True:
    if n - count > 0:
        n -= count
        count += 1
    elif n - count <= 0:
        break

if count % 2 == 1:
    print(f'{count - n + 1}/{n}')
else:
    print(f'{n}/{count - n + 1}')