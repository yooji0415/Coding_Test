def check_result(x, y, board):
    w_cnt = 0
    color_list = ["W", "B"]
    for i in range(y, y+8):
        color = color_list[i % 2]
        for j in range(x, x+8):
            if board[i][j] == color:
                w_cnt += 1
            if color == "W":
                color = "B"
            else:
                color = "W"

    b_cnt = 0
    color_list = ["B", "W"]
    for i in range(y, y+8):
        color = color_list[i % 2]
        for j in range(x, x+8):
            if board[i][j] == color:
                b_cnt += 1
            if color == "W":
                color = "B"
            else:
                color = "W"

    return min(w_cnt, b_cnt)


n, m = map(int, input().split())
board = []
for cycle in range(n):
    line = input()
    board.append(line)

result = []
for y in range(n-7):
    for x in range(m-7):
        # 시작점을 찾았다
        result.append(check_result(x, y, board))

print(min(result))
