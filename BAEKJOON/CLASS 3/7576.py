import sys
from collections import deque


def bfs_tomato_ver():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if m > nx >= 0 and n > ny >= 0 and box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                queue.append([nx, ny])


m, n = map(int, sys.stdin.readline().split())
box = []
for _ in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))

queue = deque([])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(m):
    for y in range(n):
        if box[y][x] == 1:
            queue.append([x, y])

cnt = 0
bfs_tomato_ver()
for line in box:
    for num in line:
        if num == 0:
            print(-1)
            exit(0)

    cnt = max(cnt, max(line))

print(cnt - 1)
