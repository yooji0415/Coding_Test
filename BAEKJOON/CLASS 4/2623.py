import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0 for _ in range(1 + n)]
graph = [[] for _ in range(1 + n)]
q = deque([])

for _ in range(m):
    arr = list(map(int, input().split()))[1:]
    for i in range(1, len(arr)):
        before, now = arr[i - 1], arr[i]
        indegree[now] += 1
        graph[before].append(now)

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

answer = []
while q:
    now = q.popleft()
    answer.append(now)
    for node in graph[now]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(node)

if len(answer) != n:
    print(0)
else:
    for num in answer:
        print(num)
