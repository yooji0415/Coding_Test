def find4(m, n, board):
    del_pos = []
    stop_flag = True
    dx = [0, 0, 1, 1]
    dy = [0, -1, -1, 0]
    # 제거할 상자의 좌 하단 위치를 찾는다 O(n^2)
    for y in range(1, m):
        for x in range(0, n-1):
            if board[y][x] == 0:
                continue
            test = list(set([board[y][x], board[y-1][x], board[y-1][x+1], board[y][x+1]]))
            if 0 not in test and len(test) == 1:
                for i in range(4):
                    if [y + dy[i], x + dx[i]] not in del_pos:
                        del_pos.append([y + dy[i], x + dx[i]])
                stop_flag = False

    # 바뀐 것이 없다면 return
    if stop_flag:
        return board, stop_flag, 0

    # 상자 데이터 모두 0으로 변환
    cnt = len(del_pos)
    for p in del_pos:
        board[p[0]][p[1]] = 0

    # y축 기준으로 0 위치들 정렬후 0을 위로 올리기
    del_pos.sort(key= lambda k: k[0])
    for p in del_pos:
        y_pos = p[0] - 1
        while y_pos >= 0:
            if board[y_pos][p[1]] == 0:
                break
            else:
                board[p[0]][p[1]] = board[y_pos][p[1]]
                board[y_pos][p[1]] = 0
                p[0] -= 1
                y_pos -= 1

    return board, stop_flag, cnt


def solution(m, n, board):
    answer = 0
    temp = []
    for item in board:
        temp.append(list(item))

    board = temp
    while True:
        board, stop_flag, cnt = find4(m, n, board)
        if stop_flag:
            break
        else:
            answer += cnt

    return answer

