import sys
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())
cam_direction_dict = {
    1: [1, 2, 3, 4],
    2: [1, 2],
    3: [1, 2, 3, 4],
    4: [1, 2, 3, 4],
    5: [1],
}
cam_type = []
cam_pos = []
graph = []
for y in range(N):
    line = list(map(int, input().split()))
    for x in range(len(line)):
        if line[x] != 0 and line[x] != 6:
            cam_pos.append((y, x))
            cam_type.append(line[x])
    graph.append(line)

answer = int(1e9)


def up(graph, y, x):
    for ny in range(y - 1, -1, -1):
        if graph[ny][x] == 6:
            break
        graph[ny][x] = 7


def down(graph, y, x):
    for ny in range(y + 1, N):
        if graph[ny][x] == 6:
            break
        graph[ny][x] = 7


def left(graph, y, x):
    for nx in range(x - 1, -1, -1):
        if graph[y][nx] == 6:
            break
        graph[y][nx] = 7


def right(graph, y, x):
    for nx in range(x + 1, M):
        if graph[y][nx] == 6:
            break
        graph[y][nx] = 7


def check(select_arr):
    temp_graph = deepcopy(graph)
    for i in range(len(select_arr)):
        y, x = cam_pos[i]
        t = cam_type[i]
        select = select_arr[i]
        # 1번
        if t == 1:
            if select == 1:
                right(temp_graph, y, x)
            elif select == 2:
                up(temp_graph, y, x)
            elif select == 3:
                left(temp_graph, y, x)
            else:
                down(temp_graph, y, x)
        # 2번
        elif t == 2:
            if select == 1:
                right(temp_graph, y, x)
                left(temp_graph, y, x)
            else:
                up(temp_graph, y, x)
                down(temp_graph, y, x)
        # 3번
        elif t == 3:
            if select == 1:
                up(temp_graph, y, x)
                right(temp_graph, y, x)
            elif select == 2:
                up(temp_graph, y, x)
                left(temp_graph, y, x)
            elif select == 3:
                left(temp_graph, y, x)
                down(temp_graph, y, x)
            else:
                down(temp_graph, y, x)
                right(temp_graph, y, x)
        # 4번
        elif t == 4:
            if select == 1:
                up(temp_graph, y, x)
                right(temp_graph, y, x)
                left(temp_graph, y, x)
            elif select == 2:
                up(temp_graph, y, x)
                left(temp_graph, y, x)
                down(temp_graph, y, x)
            elif select == 3:
                left(temp_graph, y, x)
                down(temp_graph, y, x)
                right(temp_graph, y, x)
            else:
                down(temp_graph, y, x)
                right(temp_graph, y, x)
                up(temp_graph, y, x)
        # 5번
        else:
            left(temp_graph, y, x)
            down(temp_graph, y, x)
            right(temp_graph, y, x)
            up(temp_graph, y, x)

    result = 0
    # 개수 체크
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                result += 1

    return result


def back_tracking(idx, select_arr):
    global answer
    if idx == len(cam_type):
        result = check(select_arr)
        answer = result if result < answer else answer
        return

    for d in cam_direction_dict[cam_type[idx]]:
        back_tracking(idx + 1, select_arr + [d])

    return


back_tracking(0, [])
print(answer)
