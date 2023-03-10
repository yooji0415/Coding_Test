import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

tetros = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [1, 0], [2, 0], [2, -1]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [-1, 1], [-1, 2]],
    [[0, 0], [1, 0], [1, -1], [2, -1]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [0, 1], [-1, 1], [1, 1]],
    [[0, 0], [0, 1], [-1, 1], [0, 2]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
]

answer = 0

for x in range(N):
    for y in range(M):
        for tetro in tetros:
            temp_sum = 0
            flag = False

            for dx, dy in tetro:
                nx, ny = dx + x, dy + y
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    flag = True
                    break
                temp_sum += graph[nx][ny]

            if flag:
                continue

            answer = temp_sum if answer < temp_sum else answer

print(answer)