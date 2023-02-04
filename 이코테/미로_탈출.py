n, m = map(int, input().split())
graph = []
cnt_graph = [[1000000 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, list(input()))))

cnt_graph[0][0] = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    global cnt_graph
    queue = [(0, 0)]
    while queue:
        y, x = queue.pop()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= n:
                continue
            if nx < 0 or nx >= m:
                continue
            if graph[ny][nx] == 1 and cnt_graph[ny][nx] > cnt_graph[y][x] + 1:
                cnt_graph[ny][nx] = cnt_graph[y][x] + 1
                queue.append((ny, nx))


bfs()
print(cnt_graph[n - 1][m - 1])