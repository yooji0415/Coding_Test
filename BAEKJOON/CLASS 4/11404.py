import sys

INF = sys.maxsize


def floyd():
    dist = [[INF] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = first[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
first = [[INF] * n for i in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if first[a-1][b-1] != INF:
        first[a-1][b-1] = min(first[a-1][b-1], c)
    else:
        first[a-1][b-1] = c

result = floyd()

for i in range(n):
    for j in range(n):
        if i == j or result[i][j] == INF:
            print(0, end=" ")
        else:
            print(result[i][j], end=" ")

    print()
