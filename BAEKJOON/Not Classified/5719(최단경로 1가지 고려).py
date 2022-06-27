import sys
import heapq


def dijkstra(graph, start):
    distances = {node: 100000000 for node in graph}
    distances[start] = 0
    route = {node: [] for node in graph}
    queue = []
    heapq.heappush(queue, [distances[start], start])
    route[start].append(start)
    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                route[new_destination] = route[current_destination] + [new_destination]
                heapq.heappush(queue, [distance, new_destination])

    return distances, route


while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    graph = {x: {} for x in range(n)}
    s, d = map(int, sys.stdin.readline().split())
    for _ in range(m):
        u, v, p = map(int, sys.stdin.readline().split())
        graph[u][v] = p

    result_distance, result_route = dijkstra(graph, s)
    print(graph)
    if result_distance[d] == 100000000:
        print(-1)
        continue
    for i in range(1, len(result_route[d])):
        del graph[result_route[d][i - 1]][result_route[d][i]]

    result_distance, result_route = dijkstra(graph, s)
    print(graph)
    if result_distance[d] == 100000000:
        print(-1)
        continue
    else:
        print(result_distance[d])

