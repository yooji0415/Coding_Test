from collections import deque


def bfs(n, graph):
    queue = deque()
    queue.append(1)
    distance = [-1] * (n + 1)
    distance[1] = 0
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if distance[node] == -1:
                distance[node] = distance[now] + 1
                queue.append(node)

    return distance


def solution(n, edge):
    graph = {x: [] for x in range(1, n + 1)}
    for e in edge:
        n1, n2 = e[0], e[1]
        graph[n1].append(n2)
        graph[n2].append(n1)

    answer_list = bfs(n, graph)
    answer_list.sort(reverse=True)

    return answer_list.count(answer_list[0])
