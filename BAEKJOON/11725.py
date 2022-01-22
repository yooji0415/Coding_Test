import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if parent[i] == 0:
                parent[i] = node
                q.append(i)

    return parent

bfs()

for i in parent[2:]:
    print(i)