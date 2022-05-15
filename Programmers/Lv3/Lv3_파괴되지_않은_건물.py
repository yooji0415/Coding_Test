def solution(board, skill):
    answer = 0
    degree_board = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    for s in skill:
        tp, r1, c1, r2, c2, degree = s[0], s[1], s[2], s[3], s[4], s[5]
        if tp == 1:
            degree_board[r1][c1] -= degree
            degree_board[r1][c2 + 1] += degree
            degree_board[r2 + 1][c1] += degree
            degree_board[r2 + 1][c2 + 1] -= degree
        else:
            degree_board[r1][c1] += degree
            degree_board[r1][c2 + 1] -= degree
            degree_board[r2 + 1][c1] -= degree
            degree_board[r2 + 1][c2 + 1] += degree

    for i in range(len(degree_board)):
        for j in range(1, len(degree_board[0])):
            degree_board[i][j] += degree_board[i][j - 1]

    for i in range(1, len(degree_board)):
        for j in range(len(degree_board[0])):
            degree_board[i][j] += degree_board[i - 1][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += degree_board[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
