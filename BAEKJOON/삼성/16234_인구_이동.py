import sys
import copy
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = []
visited = [[False] * N for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs(start_x, start_y, next_graph):
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True
    total = graph[start_x][start_y]
    pos = [(start_x, start_y)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue

            if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                q.append((nx, ny))
                visited[nx][ny] = True
                pos.append((nx, ny))
                total += graph[nx][ny]

    if len(pos) == 1:
        return False

    result = total // len(pos)
    for x, y in pos:
        next_graph[x][y] = result

    return True


flag = True
cnt = 0

while flag:
    flag = False
    visited = [[False] * N for _ in range(N)]
    next_graph = copy.deepcopy(graph)
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                is_work = bfs(x, y, next_graph)
                if is_work:
                    flag = True

    if flag:
        graph = next_graph
        cnt += 1

print(cnt)
