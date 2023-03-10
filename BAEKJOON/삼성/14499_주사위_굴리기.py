import sys

input = sys.stdin.readline

# 세로 N, 가로 M, x, y, 명령수 K
N, M, x, y, k = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 1 동쪽 / 2 서쪽 / 3 북쪽 / 4 남쪽
commands = list(map(int, input().split()))
d = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]

# 일단 움직이는 메커니즘을 만들어보자
# 이후 주사위를 저장을 해야하는데 어떻게 해야 잘 저장할까
# 주어진 모양을 그대로 사용해보자
dice = [[0], [0, 0, 0], [0], [0]]


# 좌 우로 굴릴 경우
def roll_right(nx, ny):
    global dice
    pos_data = graph[nx][ny]
    dice = [dice[0], [dice[3][0], dice[1][0], dice[1][1]], dice[2], [dice[1][2]]]
    if pos_data == 0:
        graph[nx][ny], dice[3][0] = dice[3][0], dice[3][0]
    else:
        graph[nx][ny], dice[3][0] = 0, graph[nx][ny]


def roll_left(nx, ny):
    global dice
    pos_data = graph[nx][ny]
    dice = [dice[0], [dice[1][1], dice[1][2], dice[3][0]], dice[2], [dice[1][0]]]
    if pos_data == 0:
        graph[nx][ny], dice[3][0] = dice[3][0], dice[3][0]
    else:
        graph[nx][ny], dice[3][0] = 0, graph[nx][ny]


# 상 하로 굴릴 경우
def roll_up(nx, ny):
    global dice
    pos_data = graph[nx][ny]
    dice = [[dice[1][1]], [dice[1][0], dice[2][0], dice[1][2]], dice[3], dice[0]]
    if pos_data == 0:
        graph[nx][ny], dice[3][0] = dice[3][0], dice[3][0]
    else:
        graph[nx][ny], dice[3][0] = 0, graph[nx][ny]


def roll_down(nx, ny):
    global dice
    pos_data = graph[nx][ny]
    dice = [[dice[3][0]], [dice[1][0], dice[0][0], dice[1][2]], [dice[1][1]], dice[2]]
    if pos_data == 0:
        graph[nx][ny], dice[3][0] = dice[3][0], dice[3][0]
    else:
        graph[nx][ny], dice[3][0] = 0, graph[nx][ny]


# def print_graph():
#     for line in graph:
#         print(line)


# print("original")
# print(dice)
# print_graph()
for command in commands:
    dx, dy = d[command]
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    if command == 1:
        # print("right")
        roll_right(nx, ny)
    if command == 2:
        # print("left")
        roll_left(nx, ny)
    if command == 3:
        # print("up")
        roll_up(nx, ny)
    if command == 4:
        # print("down")
        roll_down(nx, ny)

    # print(dice)
    # print_graph()
    x, y = nx, ny
    print(dice[1][1])
