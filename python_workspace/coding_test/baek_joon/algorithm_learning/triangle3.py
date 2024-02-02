msg = ['Invalid', 'Scalene', 'Isosceles', 'Equilateral']

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if a + b <= c or a + c <= b or b + c <= a:
        print(msg[0])
    elif a == b == c:
        print(msg[3])
    elif a == b or a == c or b == c:
        print(msg[2])
    else:
        print(msg[1])