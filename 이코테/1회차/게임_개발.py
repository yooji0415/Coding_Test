n, m = map(int, input().split())
y, x, d = map(int, input().split())
# 방향은 0 북 1 동 2 남 3 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

cnt = 1
visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
visited[y][x] = True
no_cnt = 0
while True:
    if no_cnt == 4:
        no_cnt = 0
        x, y = x - dx[d], y - dy[d]
        # print("no cnt is 4 so move x: {} y: {} d: {}".format(x, y, d))
        if x < 0 or x >= len(graph[0]):
            break
        if y < 0 or y >= len(graph):
            break
        if graph[y][x] == 1:
            break

    d = d - 1 if d != 0 else 3
    n_y, n_x = y + dy[d], x + dx[d]
    # print("x: {} y: {} d: {}".format(n_x, n_y, d))
    if n_y < 0 or n_y >= len(graph) or n_x < 0 or n_x >= len(graph[0]):
        # print("out 1")
        no_cnt += 1
        continue
    if graph[n_y][n_x] == 1 or visited[n_y][n_x]:
        # print("out 2")
        no_cnt += 1
        continue

    # print("success")
    cnt += 1
    no_cnt = 0
    visited[n_y][n_x] = True
    y, x = n_y, n_x

print(cnt)
