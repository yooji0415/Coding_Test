def find(y, x, cnt, temp):
    if cnt == 7:
        candi.append(temp)
    else:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if -1 < nx < 4 and -1 < ny < 4:
                find(ny, nx, cnt + 1, temp + board[ny][nx])


t = int(input())
for i in range(1, t + 1):
    board = []
    for _ in range(4):
        line = input().split(' ')
        board.append(line)
    candi = []
    for y in range(4):
        for x in range(4):
            find(y, x, 1, board[y][x])

    print(f"#{i} {len(set(candi))}")
