

def is_prime_sq(num):
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

    pass

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