def solution(maps):
    from collections import deque
    max_row, max_col = len(maps), len(maps[0])
    visited = [[False for _ in range(max_col)] for _ in range(max_row)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    def bfs():
        bfs_depth = 1
        queue = deque()
        queue.append([0, 0])

        queue_size = len(queue)

        while queue:
            curr_r, curr_c = queue.popleft()
            if queue_size == 0:
                queue_size = len(queue)
                bfs_depth += 1
            else:
                queue_size -= 1

            for i in range(4):
                next_r, next_c = curr_r + dr[i], curr_c + dc[i]
                if next_r in [-1, max_row] or next_c in [-1, max_col]:
                    continue
                if next_r == max_row - 1 and next_c == max_col - 1:
                    return bfs_depth + 1
                if not visited[next_r][next_c] and maps[next_r][next_c] == 1:
                    visited[next_r][next_c] = True  # 이렇게 하는게 curr_r, curr_c 수준에서 방문 처리하는 것 보다 성능이 좋다(중복 제외처리해주기 때문)
                    queue.append([next_r, next_c])

        return -1

    return bfs()


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
