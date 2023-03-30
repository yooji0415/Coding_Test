from collections import deque
# 도시, 도로, 타겟 거리, 출발
n, m, target, start = map(int,input().split())
dist = [-1] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 거리
    graph[a].append(b)

q = deque([start])
dist[start] = 0

while q:
    now = q.popleft()
    for candi in graph[now]:
        length = dist[now] + 1
        if length < dist[candi] or dist[candi] == -1:
            dist[candi] = length
            q.append(candi)

check = True
for i in range(1, n + 1):
    if dist[i] == target:
        check = False
        print(i)

if check:
    print(-1)
