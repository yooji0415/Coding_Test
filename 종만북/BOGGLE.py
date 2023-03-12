import sys

c = int(sys.stdin.readline())
dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]
board = []


def range_check(x, y):
    if y < 0 or y >= 5:
        return False
    if x < 0 or x >= 5:
        return False
    return True


def word_check(x, y, word):
    if not range_check(x, y):
        return False
    if board[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True
    for i in range(8):
        n_x, n_y = x + dx[i], y + dy[i]
        if word_check(n_x, n_y, word[1:]):
            return True
    return False


def check_all_board(word):
    for i in range(5):
        for j in range(5):
            if word_check(i, j, word):
                return True
    return False


for _ in range(c):
    board = []
    for _ in range(5):
        board.append(list(sys.stdin.readline().strip()))
    w_len = int(sys.stdin.readline())
    words = []
    for _ in range(w_len):
        word = sys.stdin.readline().strip()
        words.append(word)
    answer = []
    for word in words:
        answer.append(check_all_board(word))

    for i in range(len(words)):
        print('{} {}'.format(words[i], 'YES' if answer[i] else 'NO'))

