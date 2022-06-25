import sys
from collections import deque


def bfs(s):
    q = deque([s])
    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            print(v, end=" ")
            for e in graph[v]:
                if not visited[e]:
                    q.append(e)
    return 0


def dfs(s):
    print(s, end=" ")
    visited[s] = True
    for e in graph[s]:
        if not visited[e]:
            dfs(e)
    return 0


n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for e in graph:
    e.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
