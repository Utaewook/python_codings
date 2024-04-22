# import sys
# input = sys.stdin.readline
#
# primes = set()
#
# def partition(num):
#     count = 0
#
#     for i in range(2, num//2 + 1):
#         if i in primes and num-i in primes:
#             count += 1
#
#     return count
#
#
# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#
#     i = 5
#
#     while i*i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#
#     return True
#
# for i in range(2, 1000000):
#     if is_prime(i):
#         primes.add(i)
#
#
# for _ in range(int(input())):
#     n = int(input())
#     print(partition(n))

# 에라토스테네스의 체

import sys
input = sys.stdin.readline


def is_prime_eratos(n):  # 0~n 범위 내의 소수를 출력
    is_prime = [True] * (n+1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            # Updating all multiples of p to not prime
            for i in range(p * p, n+1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n+1) if is_prime[p]]
    return prime_numbers


for _ in range(int(input())):
    num = int(input())

    primes = is_prime_eratos(num - 2)

    count = 0
    for i in range(len(primes)//2 + 1):
        if num - primes[i] in primes:
            count += 1
    print(count)