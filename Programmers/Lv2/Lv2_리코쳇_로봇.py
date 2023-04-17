from collections import deque


def solution(board):
    answer = 0

    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == "R":
                start_x = x
                start_y = y
            if board[x][y] == "G":
                end_x = x
                end_y = y

    def bfs(board, x, y, end_x, end_y):
        ROW = len(board)
        COL = len(board[0])
        q = deque()
        q.append((x, y, 0))
        visited = [[-1] * COL for _ in range(ROW)]
        visited[x][y] = 0
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        while q:
            now_x, now_y, cost = q.popleft()
            for i in range(4):
                nx, ny = now_x, now_y
                while 0 <= nx + dx[i] < ROW and 0 <= ny + dy[i] < COL and board[nx + dx[i]][ny + dy[i]] != "D":
                    nx += dx[i]
                    ny += dy[i]
                if visited[nx][ny] != -1:
                    continue
                visited[nx][ny] = cost + 1
                q.append((nx, ny, cost + 1))

        if visited[end_x][end_y] == -1:
            return -1
        return visited[end_x][end_y]

    return bfs(board, start_x, start_y, end_x, end_y)