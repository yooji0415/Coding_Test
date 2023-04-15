import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(graph, n, m):
    q = deque()
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = 0
    condition = [[0] * m for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                condition[nx][ny] += 1
                continue
            else:
                visited[nx][ny] = True
                q.append((nx, ny))
    return condition


def simulation(graph, n, m, condition):
    flag = True
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                continue
            else:
                if condition[x][y] > 1:
                    graph[x][y] = 0
                else:
                    flag = False
    return flag


def solution(n, m, graph):
    answer = 0
    flag = False
    while not flag:
        answer += 1
        condition = bfs(graph, n, m)
        flag = simulation(graph, n, m, condition)
    return answer


print(solution(n, m, graph))
