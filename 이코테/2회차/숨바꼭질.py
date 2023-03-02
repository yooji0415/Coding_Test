import heapq


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))

distance = [INF] * (n + 1)
# 거리, 노드 번호 순
q = [(0, 1)]
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)
    if dist < distance[now]:
        continue

    for (cost, node) in graph[now]:
        next_cost = cost + dist
        if distance[node] > next_cost:
            distance[node] = next_cost
            heapq.heappush(q, (next_cost, node))

answer_cost = 0
answer_node = 0
answer_cnt = 0
for i in range(2, n + 1):
    cost = distance[i]
    if cost != INF and answer_cost < cost:
        answer_cost = cost
        answer_node = i
        answer_cnt = 1
    elif answer_cost == cost:
        answer_cnt += 1

print(distance[1:])
print(f"{answer_node} {answer_cost} {answer_cnt}")
