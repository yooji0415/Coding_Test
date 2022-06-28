import sys
from collections import deque


def bfs(v):
    q = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True
    cnt = 1
    while q:
        v = q.popleft()
        for e in graph[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                cnt += 1

    return cnt


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[e].append(s)

answer_list = []
max_cnt = -1
for i in range(1, n + 1):
    result = bfs(i)
    if max_cnt <= result:
        if max_cnt == result:
            answer_list.append(i)
        else:
            max_cnt = result
            answer_list = [i]

for answer in answer_list:
    print(answer, end=" ")
