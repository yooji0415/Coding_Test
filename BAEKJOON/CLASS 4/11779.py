import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

distance = [INF] * (1 + n)
graph = [[] for _ in range(1 + n)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, end = map(int, input().split())
parents = {i: 0 for i in range(1, n + 1)}

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for node in graph[now]:
        cost = dist + node[1]
        if cost < distance[node[0]]:
            distance[node[0]] = cost
            heapq.heappush(q, (cost, node[0]))
            parents[node[0]] = now

temp = end
cnt = 0
route = ""
while temp != 0:
    route = str(temp) + " " + route
    cnt += 1
    temp = parents[temp]

print(distance[end])
print(cnt)
print(route)
