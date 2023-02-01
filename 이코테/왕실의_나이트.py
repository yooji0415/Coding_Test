x, y = list(input())
y = int(y) - 1
x = ord(x) - 97
# print(x, y)

graph = [[False for i in range(8)] for i in range(8)]
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
cnt = 0

graph[y][x] = True
cnt += 1
queue = [(y, x)]
while queue:
    y, x = queue.pop()
    for i in range(8):
        n_y, n_x = y + dy[i], x + dx[i]
        if 0 <= n_y < 8 and 0 <= n_x < 8:
            if not graph[n_y][n_x]:
                graph[n_y][n_x] = True
                cnt += 1
                queue.append((n_y, n_x))

print(cnt)
