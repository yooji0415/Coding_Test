from collections import deque

# 보드의 크기
N = int(input())
# 사과의 개수
K = int(input())
graph = [[0] * N for _ in range(N)]
graph[0][0] = 1
for _ in range(K):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 2
# 뱀의 방향 전환 수
L = int(input())
commands = deque()
for _ in range(L):
    x, c = input().split()
    commands.append((int(x), c))

# 오른쪽 / 아래 / 왼쪽 / 위
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0
snake = deque([[0, 0]])


def simulate():
    head_x, head_y = snake[0]
    dx, dy = d[direction]
    nx, ny = head_x + dx, head_y + dy
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        return False
    if graph[nx][ny] == 1:
        return False
    # 사과 유무에 따른 무빙의 차이를 주자
    if graph[nx][ny] == 2:
        snake.appendleft([nx, ny])
        graph[nx][ny] = 1
    else:
        snake.appendleft([nx, ny])
        graph[nx][ny] = 1
        tail_x, tail_y = snake.pop()
        graph[tail_x][tail_y] = 0
    return True


cnt = 0
flag = True
while flag:
    flag = simulate()
    cnt += 1
    if commands and commands[0][0] == cnt:
        x, c = commands.popleft()
        if c == "L":
            direction = (direction + 4 - 1) % 4
        elif c == "D":
            direction = (direction + 1) % 4

print(cnt)
