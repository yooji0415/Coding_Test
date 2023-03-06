from collections import deque

city_cnt, road_cnt, target, start = map(int, input().split())
graph = [[] for _ in range(city_cnt + 1)]

for _ in range(road_cnt):
    a, b = map(int, input().split())
    graph[a].append(b)

# bfs
visited = [False] * (city_cnt + 1)
q = deque([])
q.append((start, 0))
visited[start] = True
answer = []

while q:
    now, dist = q.popleft()
    for _next in graph[now]:
        if visited[_next]:
            continue
        _next_dist = dist + 1
        if _next_dist == target:
            answer.append(_next)
        q.append((_next, _next_dist))
        visited[_next] = True

if not answer:
    print(-1)
else:
    for node in answer:
        print(node)
