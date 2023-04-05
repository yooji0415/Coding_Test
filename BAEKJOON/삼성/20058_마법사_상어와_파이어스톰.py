n, q = map(int, input().split())
n = 2 ** n

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def turn_all(graph, l):
    new_graph = [[0] * n for _ in range(n)]
    row = 2 ** l
    col = 2 ** l
    for start_x in range(0, n, row):
        for start_y in range(0, n, col):
            for x in range(row):
                for y in range(col):
                    new_graph[start_x + y][start_y + row - x - 1] = graph[start_x + x][start_y + y]
    return new_graph


def melt(graph):
    new_graph = [[0] * n for _ in range(n)]
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    for x in range(n):
        for y in range(n):
            cnt = 0
            if graph[x][y] == 0:
                continue
            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    cnt += 1
                    continue
                if graph[nx][ny] == 0:
                    cnt += 1
            if cnt <= 1:
                new_graph[x][y] = graph[x][y]
            else:
                new_graph[x][y] = graph[x][y] - 1
    return new_graph


def dfs(graph, x, y, visited):
    stack = [(x, y)]
    visited[x][y] = True
    cnt = 1

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    while stack:
        now_x, now_y = stack.pop()
        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))
                cnt += 1
    return cnt


commands = list(map(int, input().split()))

for command in commands:
    graph = turn_all(graph, command)
    graph = melt(graph)

visited = [[False] * n for _ in range(n)]
answer = 0
total = 0
for x in range(n):
    for y in range(n):
        total += graph[x][y]
        if not visited[x][y] and graph[x][y] != 0:
            result = dfs(graph, x, y, visited)
            answer = max(answer, result)

print(total)
print(answer)