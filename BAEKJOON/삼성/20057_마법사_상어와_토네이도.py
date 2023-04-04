n = int(input())
graph = []
for _ in range(n):
    array = list(map(int, input().split()))
    graph.append(array)

x = n // 2
y = n // 2
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
d = 0
swip = {
    0: [(-2, 0, 2), (-1, -1, 10), (-1, 0, 7), (-1, 1, 1), (0, -2, 5), (1, -1, 10), (1, 0, 7), (1, 1, 1), (2, 0, 2)],
    1: [(0, -2, 2), (1, -1, 10), (0, -1, 7), (-1, -1, 1), (2, 0, 5), (1, 1, 10), (0, 1, 7), (-1, 1, 1), (0, 2, 2)],
    2: [(-2, 0, 2), (-1, 1, 10), (-1, 0, 7), (-1, -1, 1), (0, 2, 5), (1, 1, 10), (1, 0, 7), (1, -1, 1), (2, 0, 2)],
    3: [(0, -2, 2), (-1, -1, 10), (0, -1, 7), (1, -1, 1), (-2, 0, 5), (-1, 1, 10), (0, 1, 7), (1, 1, 1), (0, 2, 2)]
}

answer = 0


def move(graph, d, x, y):
    global answer
    original = graph[x][y]
    graph[x][y] = 0
    remain = original
    for dx, dy, percent in swip[d]:
        nx, ny = dx + x, dy + y
        send = int(original * percent / 100)
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            answer += send
            remain -= send
            continue
        graph[nx][ny] += send
        remain -= send
    a_x, a_y = x + directions[d][0], directions[d][1] + y
    if a_x < 0 or a_x >= n or a_y < 0 or a_y >= n:
        answer += remain
    else:
        graph[a_x][a_y] += remain


index = 0
while (n // 2) * 4 >= index:
    for _ in range(1 + index // 2):
        x = directions[d][0] + x
        y = directions[d][1] + y
        if y < 0:
            break
        move(graph, d, x, y)
    d = (d + 1) % 4
    index += 1
    # print(index)
    # for line in graph:
    #     print(line)
    # print()

print(answer)
