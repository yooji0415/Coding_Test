from collections import deque

n, k = map(int, input().split())
graph = []
virus_graph = [[0] * n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

s, target_x, target_y = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs_virus(x, y, v_type):
    q = deque([(x, y)])
    virus_graph[y][x] = (v_type, 0)
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            # 범위를 벗어난 경우면
            if nx < 0 or nx >= n or ny >= n or ny < 0:
                continue
            # 만약 해당 위치가 이미 점령된 경우
            if virus_graph[ny][nx] != 0:
                nv, cnt = virus_graph[ny][nx]
                # 해당 위치가 시간이 낮은 경우
                if cnt < virus_graph[now_y][now_x][1] + 1:
                    continue
                # 시간이 같지만 숫자가 작은 경우
                if cnt == virus_graph[now_y][now_x][1] + 1 and v_type > nv:
                    continue
            # 이제는 그 위치를 먹을 수 있다.
            cnt = virus_graph[now_y][now_x][1] + 1
            # 하지만 시간보다 긴 경우는 제거한다.
            if cnt > s:
                continue
            virus_graph[ny][nx] = (v_type, cnt)
            q.append((nx, ny))


for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            bfs_virus(j, i, graph[i][j])

for g in virus_graph:
    print(g)

print(virus_graph[target_y][target_x][0] if virus_graph[target_y][target_x] != 0 else 0)
