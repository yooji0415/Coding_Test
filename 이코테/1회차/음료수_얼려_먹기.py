n, m = map(int, input().split())
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, list(input()))))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(y, x):
    global visited
    visited[y][x] = True
    queue = [(y, x)]
    while queue:
        nowY, nowX = queue.pop()
        for i in range(4):
            nextY, nextX = nowY + dy[i], nowX + dx[i]
            if nextY < 0 or nextY >= n:
                continue
            if nextX < 0 or nextX >= m:
                continue
            if not visited[nextY][nextX] and graph[nextY][nowX] == 0:
                visited[nextY][nextX] = True
                queue.append((nextY, nextX))


# print(visited)
# print(graph)

cnt = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0 and not visited[y][x]:
            cnt += 1
            bfs(y, x)

print(cnt)
