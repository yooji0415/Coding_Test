import heapq

INF = int(1e9)
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
tc = int(input())
for _ in range(tc):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * n for _ in range(n)]
    q = [(graph[0][0], 0, 0)]
    distance[0][0] = graph[0][0]

    while q:
        dist, y, x = heapq.heappop(q)

        if dist < distance[y][x]:
            continue

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            cost = dist + graph[ny][nx]
            if distance[ny][nx] > cost:
                distance[ny][nx] = cost
                heapq.heappush(q, (cost, ny, nx))

    for line in distance:
        print(line)

    print(distance[n - 1][n - 1])
