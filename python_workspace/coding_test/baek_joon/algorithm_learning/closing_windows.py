import sys
input = sys.stdin.readline

n = int(input())



def eratos(num):
    is_prime = [True] * (num + 1)

    p = 2
    while p*p <= num:
        if is_prime[p]:

            for i in range(p*p, num + 1, p):
                is_prime[i] = False
        p += 1

    prime_numbers = [i for i in range(2, num + 1) if is_prime[i]]
    return prime_numbers

print(n - len(eratos(n)))