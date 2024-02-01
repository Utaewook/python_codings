def solution(numbers):
    answer = set()
    numbers = list(numbers)
    for i in range(1, len(numbers) + 1):
        answer.update(permutation(numbers, i))
    print(answer)

    return len(answer)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def permutation(arr, n):
    result = set()

    def dfs(selected, rest):
        if len(selected) == n:
            s = ''.join(selected)
            if is_prime(int(s)):
                result.add(int(s))

        for i in range(len(rest)):
            selected.append(rest[i])
            dfs(selected, rest[:i] + rest[i + 1:])
            selected.pop()

    dfs([], arr[:])
    return result