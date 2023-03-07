n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start - 1][end - 1] = min(cost, graph[start - 1][end - 1])

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for y in range(n):
    for x in range(n):
        print(graph[y][x] if graph[y][x] != INF else 0, end=" ")
    print()
