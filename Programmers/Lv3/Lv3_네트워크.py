from collections import deque


def bfs(start, graph, visited):
    queue = deque()
    visited[start] = 1
    queue.append(start)

    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if visited[node] == 0:
                visited[node] = 1
                queue.append(node)


def solution(n, computers):
    # 우선 입력을 정리한다
    graph = {}
    for i in range(len(computers)):
        computers[i][i] = 0
        temp = []
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                temp.append(j)

        graph[i] = temp

    # 이후 bfs를 위한 변수를 생성한다.
    visited = [0] * n
    i, cnt = 0, 0

    while i < n:
        if visited[i] == 0:
            cnt += 1
            bfs(i, graph, visited)

        i += 1

    return cnt

