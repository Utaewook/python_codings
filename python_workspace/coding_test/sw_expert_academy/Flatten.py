test_case = 1
while True:
    dump = input()
    if not dump:
        break
    dump = int(dump)
    wall = list(map(int,input().split()))

    for _ in range(dump):
        wall.sort()
        wall[0] += 1
        wall[-1] -= 1
    print(f"#{test_case} {wall[-1]-wall[0]}")
    test_case += 1