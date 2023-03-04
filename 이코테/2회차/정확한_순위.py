n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
for y in range(1, n + 1):
    flag = True
    for x in range(1, n + 1):
        if graph[y][x] == INF and graph[x][y] == INF:
            flag = False
            break
    if flag:
        answer += 1

print(answer)
