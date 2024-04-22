import time, sys

input = sys.stdin.readline

start = time.time()
n = int(input())
s = 0
for i in range(n):
    s += 1

end = time.time()

print(end-start, 'sec')