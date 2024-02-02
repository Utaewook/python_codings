from collections import deque

for i in range(int(input())):
    test_case, *arr = input().split()
    arr = list(map(int, arr))
    arr.reverse()

    count = 0
    line = list()
    while len(line) < 20:
        student = arr.pop()
        if not line or max(line) < student:
            line.append(student)
        else:
            for idx, l in enumerate(line):
                if l > student:
                    line.insert(idx, student)
                    count += len(line) - idx - 1
                    break

    print(test_case, count)
