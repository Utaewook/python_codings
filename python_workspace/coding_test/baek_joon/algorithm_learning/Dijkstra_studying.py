import heapq
import sys

DIS_INF = sys.maxsize


def input_graph():
    fin = open("dijkstra_graph_inputs.txt", 'r')

    n = int(fin.readline())
    m = int(fin.readline())
    graph = [[] for _ in range(n + 1)]
    weights = {}
    for _ in range(m):
        a, b, weight = map(int, fin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        weights[(a, b)] = weight
        weights[(b, a)] = weight

    fin.close()
    return graph, weights


def dijkstra(graph, weights, start, end):
    queue = []
    distance = [DIS_INF] * (len(graph))
    distance[start] = 0
    heapq.heappush(queue, (distance[start], start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        print("log - while loop", current_node, current_distance)

        if distance[current_node] < current_distance:
            continue

        for neighbor in graph[current_node]:
            edge = (current_node, neighbor)
            d = current_distance + weights[edge]
            if d < distance[neighbor]:
                distance[neighbor] = d
                heapq.heappush(queue, (d, neighbor))

    return queue, distance[end]


if __name__ == "__main__":
    G, W = input_graph()

    print("-" * 40)
    for i in range(len(G)):
        print(f"\t\tnode[{i}] : {G[i]}")
    print("-" * 40)
    for ed in W.keys():
        print(f"\t\tedge {ed}'s weight = {W[ed]}")
    print("-" * 40)

    s, e = map(int, input("enter start node & end node: ").split())
    path, cost = dijkstra(G, W, s, e)
    print(path)
    print(cost)
