from heapq import heappush, heappop

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))

distance = [int(1e9)] * (n + 1)
distance[1] = 0

q = []
heappush(q, (0, 1))
while q:
    cost, now = heappop(q)
    if distance[now] < cost:
        continue
    for dist, node in graph[now]:
        if distance[node] > dist + cost:
            distance[node] = dist + cost
            q.append((dist + cost, node))

max_val = -int(1e9)
max_idx = 0
cnt = 1
for i in range(2, n + 1):
    if distance[i] == int(1e9):
        continue
    if max_val < distance[i]:
        max_val = distance[i]
        max_idx = i
        cnt = 1
    elif max_val == distance[i]:
        cnt += 1

print(f"{max_idx} {max_val} {cnt}")
