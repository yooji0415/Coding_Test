def solution(board, moves):
    answer = 0
    bucket = []
    max_y_pos = len(board) - 1
    for x_pos in moves:
        y_pos = 0
        while y_pos < max_y_pos:
            if board[y_pos][x_pos - 1] != 0:
                break

            y_pos += 1

        if y_pos == max_y_pos and board[y_pos][x_pos - 1] == 0:
            continue

        if not bucket:
            bucket.append(board[y_pos][x_pos - 1])
        else:
            if bucket[-1] == board[y_pos][x_pos - 1]:
                bucket.pop()
                answer += 2
            else:
                bucket.append(board[y_pos][x_pos - 1])

        board[y_pos][x_pos-1] = 0

    return answer


# 모범답안
# 비슷한 풀이니 설명은 생략했다.
def best_solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer
