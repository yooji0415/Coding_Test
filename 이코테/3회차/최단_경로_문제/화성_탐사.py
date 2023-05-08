import heapq

TC = int(input())
for _ in range(TC):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    q = []
    distance = [[int(1e9)] * N for _ in range(N)]
    distance[0][0] = graph[0][0]
    heapq.heappush(q, (0, 0, graph[0][0]))
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while q:
        x, y, dist = heapq.heappop(q)
        if dist < distance[x][y]:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if distance[nx][ny] > dist + graph[nx][ny]:
                cost = dist + graph[nx][ny]
                distance[nx][ny] = cost
                q.append((nx, ny, cost))
    print(distance[N - 1][N - 1])
