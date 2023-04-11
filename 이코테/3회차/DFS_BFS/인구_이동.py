from collections import deque

N, L, R = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs(graph, union, x, y, index):
    united = [(x, y)]
    union[x][y] = index
    total = graph[x][y]
    cnt = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if union[nx][ny] == -1 and L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                q.append((nx, ny))
                union[nx][ny] = index
                united.append((nx, ny))
                total += graph[nx][ny]
                cnt += 1

    for u in united:
        ux, uy = u
        graph[ux][uy] = total // cnt


answer = 0
while True:
    union = [[-1] * N for _ in range(N)]
    index = 0
    for x in range(N):
        for y in range(N):
            if union[x][y] == -1:
                bfs(graph, union, x, y, index)
                index += 1
    if index == N * N:
        break
    else:
        answer += 1

print(answer)
