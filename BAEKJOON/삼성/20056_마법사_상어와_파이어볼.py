# n = 행, 열 / m = 파이어볼 수 / k = 이동 횟수
n, m, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append([[] for _ in range(n)])

directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(m):
    # r = 행 / c = 열 / m = 질량 / d = 방향 / s = 속력
    r, c, m, s, d = map(int, input().split())
    graph[r - 1][c - 1].append([m, s, d])


def calc(graph, n):
    result_graph = []
    for _ in range(n):
        result_graph.append([[] for _ in range(n)])

    for x in range(n):
        for y in range(n):
            if not graph[x][y]:
                continue
            if len(graph[x][y]) == 1:
                result_graph[x][y] = graph[x][y]
                continue
            total_m = 0
            total_s = 0
            array_d = []
            for fire_ball in graph[x][y]:
                total_m += fire_ball[0]
                total_s += fire_ball[1]
                array_d.append(fire_ball[2])
            new_m = total_m // 5
            new_s = total_s // len(graph[x][y])
            if new_m == 0:
                continue
            is_same = True
            for i in range(1, len(array_d)):
                if array_d[i] % 2 != array_d[i - 1] % 2:
                    is_same = False
                    break
            if is_same:
                for i in range(4):
                    result_graph[x][y].append([new_m, new_s, i * 2])
            else:
                for i in range(4):
                    result_graph[x][y].append([new_m, new_s, i * 2 + 1])
    return result_graph


def move(graph, n):
    move_graph = []
    for _ in range(n):
        move_graph.append([[] for _ in range(n)])
    for x in range(n):
        for y in range(n):
            if not graph[x][y]:
                continue
            for fire_ball in graph[x][y]:
                m, s, d = fire_ball
                dx, dy = directions[d]
                nx, ny = x + dx * s, y + dy * s
                if nx < 0 or nx >= n:
                    if nx < 0:
                        nx = (nx + n) % n
                    else:
                        nx = nx % n
                if ny < 0 or ny >= n:
                    if ny < 0:
                        ny = (ny + n) % n
                    else:
                        ny = ny % n
                move_graph[nx][ny].append([m, s, d])
    return calc(move_graph, n)


# for line in graph:
#     print(line)
# print()

for _ in range(k):
    graph = move(graph, n)
    # for line in graph:
    #     print(line)
    # print()

answer = 0
for x in range(n):
    for y in range(n):
        if not graph[x][y]:
            continue
        for fire_ball in graph[x][y]:
            answer += fire_ball[0]
print(answer)