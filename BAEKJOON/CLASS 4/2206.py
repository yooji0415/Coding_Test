import sys
from collections import deque


def bfs(sx, sy, sz):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append([sx, sy, sz])

    while queue:
        x, y, z = queue.popleft()
        # print(x, y, z)
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < n and -1 < ny < m:
                if graph[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    queue.append([nx, ny, 1])

                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx, ny, z])

    return -1


n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().strip()))))

print(bfs(0, 0, 0))
