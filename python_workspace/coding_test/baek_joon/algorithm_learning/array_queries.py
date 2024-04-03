import sys
input = sys.stdin.readline

for test_case in range(int(input())):
    n, q = map(int, input().split())
    array = list(map(int,input().split()))

    for _ in range(q):
        line = list(map(int, input().split()))

        if line[0] == 1:
            for i in range(line[1]-1, line[2]):
                array[i] = int(array[i] ** 0.5)
        elif line[0] == 2:
            print(sum(array[line[1]-1: line[2]]))
        else:
            for i in range(line[1]-1, line[2]):
                array[i] += line[3]