from heapq import *

def solution(n, s, a, b, fares):
    FARE_INF = 100001
    graph = [[0 if i==j else FARE_INF for j in range(n + 1)] for i in range(n + 1)]
    for c,d,f in fares:
        graph[c][d] = f
        graph[d][c] = f

    def dijkstra(u, v):
        dist = [FARE_INF for _ in range(n+1)]
        dist[u] = 0
        queue = [(0, u)]

        while queue:
            curr_f, curr_node = heappop(queue)

            if curr_f > dist[curr_node]:
                continue

            for neighbor, fare in enumerate(graph[curr_node]):
                if fare > 0 and dist[curr_node] + fare < dist[neighbor]:
                    dist[neighbor] = dist[curr_node] + fare
                    heappush(queue, (dist[neighbor], neighbor))

        print(dist, dist[v])
        return dist[v]

    fare_sa, fare_sb, fare_ab, fare_ba = dijkstra(s,a),dijkstra(s,b),dijkstra(a,b), dijkstra(b,a)

    return min([fare_sa+fare_ab, fare_sb+fare_ab, fare_sb+fare_sa])


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))

