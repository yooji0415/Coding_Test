def solution(board):
    b = [[0] * (len(board[0]) + 1)]
    for i in range(len(board)):
        temp = [0]
        temp += board[i]
        b.append(temp)

    best = 0
    for y in range(1, len(b)):
        for x in range(1, len(b[y])):
            if b[y][x] == 1:
                b[y][x] = min(b[y - 1][x], b[y][x - 1], b[y - 1][x - 1]) + 1
                if best < b[y][x]:
                    best = b[y][x]

    return best ** 2

