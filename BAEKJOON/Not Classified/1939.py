import sys
from collections import deque


def bfs(C):
    queue = deque()
    queue.append(s_node)
    visited = [False] * (N + 1)
    visited[s_node] = True
    while queue:
        temp = queue.popleft()
        for n_node, weight in graph[temp]:
            if not visited[n_node] and weight >= C:
                visited[n_node] = True
                queue.append(n_node)

    return visited[e_node]


N, M = map(int, sys.stdin.readline().split(" "))
start = 1000000000
end = 1
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    # A, B는 섬 C는 무게
    A, B, C = map(int, sys.stdin.readline().split(" "))
    graph[A].append((B, C))
    graph[B].append((A, C))
    start = min(start, C)
    end = max(end, C)

s_node, e_node = map(int, sys.stdin.readline().split())
answer = start
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
