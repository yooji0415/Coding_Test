from collections import deque

n, m = map(int, input().split())
graph = []
virus = []

for x in range(n):
    line = list(map(int, input().split()))
    for y in range(n):
        if line[y] == 2:
            virus.append((x, y))
    graph.append(line)

answer = int(1e9)


def virus_simulate(virus):
    q = deque()
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    visited = [[-1] * n for _ in range(n)]
    for v in virus:
        q.append((v[0], v[1], 0))
        visited[v[0]][v[1]] = 0
    while q:
        x, y, cost = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1 or visited[nx][ny] != -1:
                continue
            q.append((nx, ny, cost + 1))
            visited[nx][ny] = cost + 1
    flag = True
    time = 0
    for x in range(n):
        for y in range(n):
            if graph[x][y] != 0:
                continue
            if visited[x][y] == -1:
                flag = False
                break
            time = max(time, visited[x][y])
        if not flag:
            break
    if not flag:
        return -1
    else:
        return time


def dfs(last_idx, nums):
    global answer
    if len(nums) == m:
        temp_virus = []
        for num in nums:
            temp_virus.append(virus[num])
        result = virus_simulate(temp_virus)
        if result != -1:
            answer = min(answer, result)
        return

    for i in range(last_idx + 1, len(virus)):
        nums.append(i)
        dfs(i, nums)
        nums.pop()
    return


dfs(-1, [])
print(answer if answer != int(1e9) else -1)
