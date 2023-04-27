import sys

input = sys.stdin.readline

ROW, COL = map(int, input().split())
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
answer = 0
graph = []

for _ in range(ROW):
    graph.append(list(map(int, input().split())))


def spread_virus(graph, x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if -1 < nx < COL and -1 < ny < ROW and graph[ny][nx] == 0:
            graph[ny][nx] = 2
            spread_virus(graph, nx, ny)


def count_safe(graph):
    cnt = 0
    for y in range(ROW):
        for x in range(COL):
            if graph[y][x] == 0:
                cnt += 1

    return cnt


def back_tracking(graph, cnt):
    global answer
    if cnt == 3:
        temp = []
        for line in graph:
            temp.append(line[:])
        for y in range(ROW):
            for x in range(COL):
                if temp[y][x] == 2:
                    spread_virus(temp, x, y)

        result = count_safe(temp)
        answer = max(answer, result)
        return

    for y in range(ROW):
        for x in range(COL):
            if graph[y][x] == 0:
                graph[y][x] = 1
                back_tracking(graph, cnt + 1)
                graph[y][x] = 0


back_tracking(graph, 0)
print(answer)
