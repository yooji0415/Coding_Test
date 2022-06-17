import sys


r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

board = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
total = (c2 - c1 + 1) * (r2 - r1 + 1)
# 좌표를 지정
x = 0
y = 0
# 숫자를 지정
num = 1
max_num = 0
# 방향 결정 변수
cnt = 0
dcnt = 1
d = 0
while total > 0:
    if r1 <= y <= r2 and c1 <= x <= c2:
        total -= 1
        board[y - r1][x - c1] = num
        max_num = num
    num += 1
    cnt += 1

    y = y + dy[d]
    x = x + dx[d]

    if cnt == dcnt:
        cnt = 0
        d = (d + 3) % 4
        if d == 0 or d == 2:
            dcnt += 1

max_num_len = len(str(max_num - 1))
for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(str(board[i][j]).rjust(max_num_len), end=" ")
    print()
