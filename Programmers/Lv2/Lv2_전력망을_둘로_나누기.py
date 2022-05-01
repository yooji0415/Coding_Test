from collections import deque
import copy


def bfs_count(start, graph, n):
    count = 0
    queue = deque()
    queue.append(start)
    visited = [0 for _ in range(n + 1)]
    while queue:
        now = queue.popleft()
        count += 1
        visited[now] = 1
        for node in graph[now]:
            if visited[node] == 0:
                queue.append(node)

    return count


def solution(n, wires):
    real_graph = {x: [] for x in range(1, n + 1)}
    answer = 1000000
    for wire in wires:
        node1, node2 = wire[0], wire[1]
        real_graph[node1].append(node2)
        real_graph[node2].append(node1)

    for wire in wires:
        node1, node2 = wire[0], wire[1]
        temp_graph = copy.deepcopy(real_graph)
        temp_graph[node1].remove(node2)
        temp_graph[node2].remove(node1)
        result1 = bfs_count(node1, temp_graph, n)
        result2 = bfs_count(node2, temp_graph, n)
        if answer > abs(result1 - result2):
            answer = abs(result1 - result2)

    return answer
