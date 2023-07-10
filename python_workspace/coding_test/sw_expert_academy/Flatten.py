for test_case in range(1,11):
    dump = input()

    dump = int(dump)
    wall = list(map(int,input().split()))
    wall.sort()

    for _ in range(dump):
        wall[0] += 1
        wall[-1] -= 1
        wall.sort()
        if wall[-1]-wall[0] == 0 or wall[-1]-wall[0] == 0:
            break
    print(f"#{test_case} {wall[-1]-wall[0]}")
    test_case += 1