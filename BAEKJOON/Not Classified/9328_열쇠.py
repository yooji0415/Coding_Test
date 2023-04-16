import sys
from collections import deque

input = sys.stdin.readline
answer = 0


def unlock(w, h, graph, keys):
    for x in range(h + 2):
        for y in range(w + 2):
            if graph[x][y].lower() in keys:
                graph[x][y] = '.'
    keys.clear()


def bfs(w, h, graph, keys):
    global answer
    q = deque([(0, 0)])
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    visited[0][0] = True
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if nx < 0 or nx >= h + 2 or ny < 0 or ny >= w + 2:
                continue
            if ord('A') <= ord(graph[nx][ny]) <= ord('Z'):
                continue
            if graph[nx][ny] == '*' or visited[nx][ny]:
                continue
            if graph[nx][ny] == '$':
                answer += 1
            if ord('a') <= ord(graph[nx][ny]) <= ord('z'):
                keys.append(graph[nx][ny])
            q.append((nx, ny))
            graph[nx][ny] = '.'
            visited[nx][ny] = True


tc = int(input())
for t in range(tc):
    h, w = map(int, input().split())
    graph = [['.'] * (w + 2)]
    for _ in range(h):
        line = input().strip()
        line = '.' + line + '.'
        graph.append(list(line))
    graph.append(['.'] * (w + 2))

    keys = deque(list(input().strip()))
    answer = 0
    while keys:
        if keys[0] == "0":
            keys.clear()
        if keys:
            unlock(w, h, graph, keys)
        bfs(w, h, graph, keys)
    print(answer)
