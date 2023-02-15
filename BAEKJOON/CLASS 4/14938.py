import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
items = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
for start in range(1, n + 1):
    result = 0
    for end in range(1, n + 1):
        if graph[start][end] <= m:
            result += items[end]

    answer = max(answer, result)

print(answer)
