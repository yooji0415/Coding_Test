n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
    graph[x][x] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = min(cost, graph[a][b])

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for x in range(1, n + 1):
    for y in range(1, n + 1):
        print(0 if graph[x][y] == INF else graph[x][y], end=" ")
    print()
