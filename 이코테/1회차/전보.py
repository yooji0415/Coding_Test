INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i

    return idx


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(c)

cnt = 0
time = 0
for i in range(1, n + 1):
    if distance[i] == INF or i == c:
        continue
    cnt += 1
    time = distance[i] if time < distance[i] else time

print(f"{cnt} {time}")
