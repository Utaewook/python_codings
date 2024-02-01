def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False for _ in range(len(words))]
    from collections import deque
    queue = deque()
    queue.append(begin)
    depth = 1
    queue_size = len(queue)

    while queue:
        curr_word = queue.popleft()
        if queue_size == 0:
            queue_size = len(queue)
            depth += 1
        else:
            queue_size -= 1

        for next_word in [w for w in words if is_changeable(w,curr_word)]:
            idx = words.index(next_word)

            if next_word == target:
                return depth
            if not visited[idx]:
                visited[idx] = True
                queue.append(next_word)

    return 0


def is_changeable(x, y):
    count = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            count += 1
    return count + 1 == len(x)


print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))