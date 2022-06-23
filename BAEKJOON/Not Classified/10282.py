import sys
import heapq


def dijkstra(graph, start):
    distances = {node: 100000000 for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances


tc = int(sys.stdin.readline())
for _ in range(tc):
    n, d, c = map(int, sys.stdin.readline().split())
    graph = {x: {} for x in range(1, n + 1)}
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b][a] = s

    result = dijkstra(graph, c)
    time = 0
    cnt = 0
    for key, value in result.items():
        if value < 100000000:
            cnt += 1
            if value > time:
                time = value

    print(cnt, time)
