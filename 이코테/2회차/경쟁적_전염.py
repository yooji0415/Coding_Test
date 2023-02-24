from collections import deque


N, K = map(int,input().split())

q = deque([])
graph = []
for y in range(N):
    arr = list(map(int, input().split()))
    line = []
    for x in range(len(arr)):
        if arr[x] != 0:
            # x, y, 해당 타입, 시간 순으로 넣는다.
            q.append((x, y, arr[x], 0))
        # 타입, 시간 순으로 넣는다.
        line.append((arr[x], 0))
    graph.append(line)

stop, target_y, target_x = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while q:
    x, y, t, time = q.popleft()
    # 시간을 넘었으면 무시
    if time >= stop:
        continue

    for i in range(4):
        n_x, n_y = x + dx[i], y + dy[i]
        if n_x < 0 or n_x >= N or n_y < 0 or n_y >= N:
            continue
        # 일단 해당 위치를 파악한다.
        now_type, now_time = graph[n_y][n_x]
        # 만약 0 이면
        if now_type == 0:
            graph[n_y][n_x] = (t, time + 1)
            q.append((n_x, n_y, t, time + 1))
            continue
        # 만약 기존 위치에 다른게 있었다는 이야기
        # 그러면 시간이 낮은 경우와 시간이 같지만 타입의 숫자가 낮은 경우를 처리
        if now_time > time + 1:
            graph[n_y][n_x] = (t, time + 1)
            q.append((n_x, n_y, t, time + 1))
            continue
        if now_time == time + 1 and t <= now_type:
            graph[n_y][n_x] = (t, time + 1)
            q.append((n_x, n_y, t, time + 1))
            continue

for line in graph:
    print(line)

print(graph[target_y - 1][target_x - 1][0])
