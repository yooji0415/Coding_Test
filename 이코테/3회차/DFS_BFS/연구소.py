ROW, COL = map(int, input().split())
graph = []
answer = 0
for _ in range(ROW):
    graph.append(list(map(int, input().split())))


def virus(graph, x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= ROW or ny < 0 or ny >= COL:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            virus(graph, nx, ny)


def dfs(graph, cnt, last_x, last_y):
    global answer

    if cnt == 3:
        temp = [[0] * COL for _ in range(ROW)]
        # 옮겨 담기
        for x in range(ROW):
            for y in range(COL):
                temp[x][y] = graph[x][y]
        # 바이러스 처리
        for x in range(ROW):
            for y in range(COL):
                if temp[x][y] == 2:
                    virus(temp, x, y)
        # 0의 수
        result = 0
        for x in range(ROW):
            for y in range(COL):
                if temp[x][y] == 0:
                    result += 1
        answer = max(answer, result)
        return

    for x in range(ROW):
        for y in range(COL):
            if x < last_x:
                continue
            if x == last_x and y < last_y:
                continue
            if graph[x][y] == 0:
                graph[x][y] = 1
                dfs(graph, cnt + 1, x, y)
                graph[x][y] = 0
    return


dfs(graph, 0, 0, 0)
print(answer)
