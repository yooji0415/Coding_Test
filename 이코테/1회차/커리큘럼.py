from collections import deque

n = int(input())

in_degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
result = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    result[i] = data[0]
    for x in data[1:-1]:
        in_degree[i] += 1
        graph[x].append(i)


def topology_sort():
    q = deque()

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for node in graph[now]:
            result[node] = max(result[node], result[now] + time[node])
            in_degree[node] -= 1
            if in_degree[node] == 0:
                q.append(node)

    for i in range(1, n + 1):
        print(result[i])


topology_sort()
