def check_finish(board, t):
    # 가로로 될 경우
    for x in range(3):
        flag = True
        for y in range(3):
            if board[x][y] != t:
                flag = False
                break
        if flag:
            return True
    # 세로로 될 경우
    for y in range(3):
        flag = True
        for x in range(3):
            if board[x][y] != t:
                flag = False
                break
        if flag:
            return True
    # 대각으로 될 경우
    if board[0][0] == t and board[1][1] == t and board[2][2] == t:
        return True
    if board[0][2] == t and board[1][1] == t and board[2][0] == t:
        return True

    return False


def solution(board):
    answer = 0
    o_cnt = 0
    x_cnt = 0
    # 일단 개수를 새어보자
    for x in range(3):
        for y in range(3):
            if board[x][y] == "O":
                o_cnt += 1
            if board[x][y] == "X":
                x_cnt += 1
    # 정상적이라면 o가 하나 더 많거나 수가 같아야 한다.
    if o_cnt != x_cnt + 1 and o_cnt != x_cnt:
        return 0
    # 만약 이 경우가 아니면 둘 중 누군가가 이겼을 경우를 보자
    is_o_win = check_finish(board, "O")
    is_x_win = check_finish(board, "X")
    # o가 이겼는데 수가 동일하면 에러
    if is_o_win and o_cnt == x_cnt:
        return 0
    # x가 이겼는데 o가 더 많으면 에러
    if is_x_win and o_cnt == x_cnt + 1:
        return 0
    return 1