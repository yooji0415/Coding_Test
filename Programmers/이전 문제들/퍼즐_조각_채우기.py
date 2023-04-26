import copy


def rotate(table):
    length = len(table)
    new_table = [[0] * length for _ in range(length)]
    for x in range(length):
        for y in range(length):
            new_table[y][length - x - 1] = table[x][y]
    return new_table


def dfs(table, target_num, start_x, start_y):
    stack = []
    length = len(table)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    stack.append((start_x, start_y))
    table[start_x][start_y] = 2
    result = [(0, 0)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= length or ny < 0 or ny >= length:
                continue
            if table[nx][ny] != target_num:
                continue
            table[nx][ny] = 2
            stack.append((nx, ny))
            result.append((nx - start_x, ny - start_y))
    return result


def solution(game_board, table):
    answer = 0
    finish_set = set()
    pieces = []
    for x in range(len(game_board)):
        for y in range(len(game_board)):
            if game_board[x][y] == 0:
                pieces.append(dfs(game_board, 0, x, y))

    for _ in range(4):
        table = rotate(table)
        temp = copy.deepcopy(table)
        for x in range(len(temp)):
            for y in range(len(temp)):
                if temp[x][y] == 1:
                    result = dfs(temp, 1, x, y)
                    flag = False

                    for i in range(len(pieces)):
                        if i in finish_set:
                            continue
                        piece = pieces[i]
                        if piece == result:
                            finish_set.add(i)
                            flag = True
                            break

                    if flag:
                        table = copy.deepcopy(temp)
                        answer += len(result)
                    else:
                        temp = copy.deepcopy(table)
    return answer


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]]))
