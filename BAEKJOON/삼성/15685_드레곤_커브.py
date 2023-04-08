import sys

input = sys.stdin.readline

n = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1

    move = [d]
    for _ in range(g):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i - 1] + 1) % 4)
        move.extend(temp)

    for m in move:
        nx, ny = x + dx[m], y + dy[m]
        graph[nx][ny] = 1
        x, y = nx, ny

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
            answer += 1

print(answer)
