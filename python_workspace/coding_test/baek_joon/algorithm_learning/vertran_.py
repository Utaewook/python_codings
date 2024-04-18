import sys

input = sys.stdin.readline


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def nprime(n):
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if is_prime(i):
            count += 1

    return count


while True:
    line = int(input())
    if line == 0:
        break
    print(nprime(line))
