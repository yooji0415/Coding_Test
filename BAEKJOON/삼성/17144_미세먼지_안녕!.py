# r = 행 c = 열 t = 시간
r, c, t = map(int, input().split())

graph = []
air_cleaner = []
for x in range(r):
    line = list(map(int, input().split()))
    if line[0] == -1 and not air_cleaner:
        air_cleaner = (x, 0)
    graph.append(line)


def dust(graph):
    new_graph = [[0] * c for _ in range(r)]
    air_x, air_y = air_cleaner
    new_graph[air_x][air_y], new_graph[air_x + 1][air_y] = -1, -1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for x in range(r):
        for y in range(c):
            if graph[x][y] < 1:
                continue

            now_dust = graph[x][y]
            split_dust = now_dust // 5
            cnt = 0
            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] == -1:
                    continue
                new_graph[nx][ny] += split_dust
                cnt += 1
            new_graph[x][y] += now_dust - split_dust * cnt

    return new_graph


def air_simulator(graph):
    new_graph = [[0] * c for _ in range(r)]
    air_x, air_y = air_cleaner
    # 위 공기 흐름부터
    for x in range(air_x):
        new_graph[x + 1][0] = graph[x][0]
    for y in range(c - 1, 0, -1):
        new_graph[0][y - 1] = graph[0][y]
    for x in range(air_x, 0, -1):
        new_graph[x - 1][c - 1] = graph[x][c - 1]
    for y in range(1, c - 1):
        new_graph[air_x][y + 1] = graph[air_x][y]
    # 아래 공기 흐름
    for x in range(r - 1, air_x + 1, - 1):
        new_graph[x - 1][0] = graph[x][0]
    for y in range(c - 1, 0, -1):
        new_graph[r - 1][y - 1] = graph[r - 1][y]
    for x in range(air_x + 1, r - 1):
        new_graph[x + 1][c - 1] = graph[x][c - 1]
    for y in range(1, c - 1):
        new_graph[air_x + 1][y + 1] = graph[air_x + 1][y]
    # 공기 청정기 배치
    new_graph[air_x][air_y], new_graph[air_x + 1][air_y] = -1, -1
    # 사이 공간 채우기
    for x in range(1, air_x):
        for y in range(1, c - 1):
            new_graph[x][y] = graph[x][y]

    for x in range(air_x + 2, r - 1):
        for y in range(1, c - 1):
            new_graph[x][y] = graph[x][y]

    return new_graph


for _ in range(t):
    graph = dust(graph)
    graph = air_simulator(graph)

answer = 0
for x in range(r):
    for y in range(c):
        if graph[x][y] < 1:
            continue
        answer += graph[x][y]

print(answer)
