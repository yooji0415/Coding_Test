from collections import deque

N, K = map(int, input().split())
graph = []
virus = []
for x in range(N):
    array = list(map(int, input().split()))
    line = []
    for y in range(len(array)):
        num = array[y]
        if num != 0:
            virus.append((x, y))
        line.append((num, 0))
    graph.append(line)

S, X, Y = map(int, input().split())


def bfs(graph, virus, S):
    q = deque()
    for v in virus:
        q.append(v)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while q:
        x, y = q.popleft()
        type, time = graph[x][y]
        if time == S:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny][0] == 0:
                graph[nx][ny] = (type, time + 1)
                q.append((nx, ny))
                continue
            if time + 1 < graph[nx][ny][1] or (time + 1 == graph[nx][ny][1] and type < graph[nx][ny][0]):
                graph[nx][ny] = (type, time + 1)
                q.append((nx, ny))


bfs(graph, virus, S)
print(graph[X - 1][Y - 1][0])
