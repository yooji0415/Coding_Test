from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(graph, start, visited):
    visited[start] = 0
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for node in graph[now]:
            if visited[node] != -1:
                continue
            visited[node] = visited[now] + 1
            q.append(node)


bfs(graph, X, visited)
flag = False
for i in range(1, N + 1):
    if visited[i] == K:
        flag = True
        print(i)

if not flag:
    print(-1)
