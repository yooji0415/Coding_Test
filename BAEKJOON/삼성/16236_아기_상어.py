import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
size = 2
eat_cnt = 0
pos_x = 0
pos_y = 0
graph = []
answer = 0
for x in range(N):
    line = list(map(int, input().split()))
    if 9 in line:
        y = line.index(9)
        pos_x, pos_y = x, y
        line[y] = 0
    graph.append(line)


def bfs(start_x, start_y, graph):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q.append((start_x, start_y))
    visited[start_x][start_y] = 0
    candidate = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] > size or visited[nx][ny] != -1:
                continue

            if graph[nx][ny] != 0 and graph[nx][ny] < size:
                candidate.append((visited[x][y] + 1, nx, ny))

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    return candidate


# print(bfs(pos_x, pos_y, graph))
while True:
    candidate = bfs(pos_x, pos_y, graph)
    candidate.sort(key=lambda x: (x[0], x[1], x[2]))
    # print(candidate)
    if not candidate:
        break
    cost, x, y = candidate[0]
    graph[x][y] = 0
    pos_x = x
    pos_y = y
    eat_cnt += 1
    if eat_cnt == size:
        size += 1
        eat_cnt = 0
        # print(f"size up!: {size}")
    answer += cost

print(answer)
