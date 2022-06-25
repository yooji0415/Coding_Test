import sys


# 세로크기 N 가로크기 M
N, M = map(int, sys.stdin.readline().split())
graph = []

row = 0
for _ in range(N):
    line = list(sys.stdin.readline().strip())
    if "X" not in line:
        row += 1
    graph.append(line)

col = 0
for j in range(M):
    flag = False
    for i in range(N):
        if graph[i][j] == "X":
            flag = True
            break

    if not flag:
        col += 1

print(max(col, row))
