from collections import deque


def bfs(start, board):
    N = len(board)
    visited = [[1000000 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    queue = deque()
    queue.append(start)
    while queue:
        y, x, before, cost = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            n_cost = cost + 600 if i != before else cost + 100
            if -1 < nx < N and -1 < ny < N and board[ny][nx] == 0 and visited[ny][nx] > n_cost:
                visited[ny][nx] = n_cost
                queue.append([ny, nx, i, n_cost])

    return visited[-1][-1]


def solution(board):
    return min(bfs([0, 0, 2, 0], board), bfs([0, 0, 0, 0], board))


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
