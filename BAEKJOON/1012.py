import sys

queue = []


def bfs(matrix, sx, sy):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue.append([sx, sy])
    matrix[sy][sx] = 0
    while queue:
        x = queue[0][0]
        y = queue[0][1]
        queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if m > nx >= 0 and n> ny >= 0:
                if matrix[ny][nx] == 1:
                    matrix[ny][nx] = 0
                    queue.append([nx, ny])
            else:
                continue


cycle = int(sys.stdin.readline())
for _ in range(cycle):
    cnt = 0
    m, n, l = map(int, sys.stdin.readline().split())
    matrix = [[0 for col in range(m)] for row in range(n)]
    for time in range(l):
        x, y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1

    for a in range(m):
        for b in range(n):
            if matrix[b][a] == 1:
                bfs(matrix, a, b)
                cnt += 1

    print(cnt)


