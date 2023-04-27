N = int(input())
graph = []
teachers = []

for x in range(N):
    array = input().split()
    for y in range(len(array)):
        if array[y] == "T":
            teachers.append((x, y))
    graph.append(array)
answer = False


def check(graph):
    dxs = [-1, 0, 1, 0]
    dys = [0, -1, 0, 1]
    for i in range(4):
        dx, dy = dxs[i], dys[i]
        for teacher in teachers:
            x, y = teacher
            nx, ny = x + dx, y + dy
            while -1 < nx < N and -1 < ny < N:
                if graph[nx][ny] == "O":
                    break
                if graph[nx][ny] == "S":
                    return False
                nx += dx
                ny += dy
    return True


def dfs(graph, last_x, last_y, cnt):
    global answer
    if cnt == 3:
        result = check(graph)
        answer = result
        return result

    for x in range(N):
        for y in range(N):
            if x < last_x or (x == last_x and y < last_y) or graph[x][y] != "X":
                continue
            graph[x][y] = "O"
            result = dfs(graph, x, y, cnt + 1)
            if result:
                return result
            graph[x][y] = "X"
    return False


dfs(graph, 0, 0, 0)
print("YES" if answer else "NO")
