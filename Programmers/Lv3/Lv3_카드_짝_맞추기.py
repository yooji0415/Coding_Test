from collections import deque
from itertools import permutations


def bfs(graph, x, y, target_x, target_y):
    row = 4
    col = 4
    visited = [[-1] * col for _ in range(row)]
    visited[x][y] = 0
    q = deque()
    q.append((x, y))
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while q:
        # 우선 컨트롤을 사용하는 경우
        for i in range(4):
            dx, dy = d[i]
            nx, ny = x, y
            # ctrl + 방향키
            while 0 <= nx < row and 0 <= ny < col:
                nx += dx
                ny += dy
                # 탈출 조건
                # 일단 범위를 나갔을 경우
                if nx < 0 or nx >= row or ny < 0 or ny >= col:
                    break
                # 그리고 해당 범위가 끝자락일 경우
                if (nx == 0 and dx == -1) or (nx == row - 1 and dx == 1) or (ny == 0 and dy == -1) or (ny == col - 1 and dy == 1):
                    cost = visited[x][y] + 2
                    if visited[nx][ny] == -1 or cost < visited[nx][ny]:
                        visited[nx][ny] = cost
                        q.append((nx, ny))
                        break
                # 그리고 해당 위치에 카드가 있을 경우
                if graph[nx][ny] != 0:
                    cost = visited[x][y] + 2
                    if visited[nx][ny] == -1 or cost < visited[nx][ny]:
                        visited[nx][ny] = cost
                        q.append((nx, ny))
                        break
            # 일반적인 bfs
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            cost = visited[x][y] + 2
            if visited[nx][ny] == -1 or cost < visited[nx][ny]:
                visited[nx][ny] = cost
                q.append((nx, ny))
    return visited[target_x][target_y]


def solution(board, r, c):
    answer = int(1e9)
    card_pos = {}
    for x in range(4):
        for y in range(4):
            if board[x][y] != 0:
                if board[x][y] not in card_pos:
                    card_pos[board[x][y]] = [(x, y)]
                else:
                    card_pos[board[x][y]].append((x, y))

    keys = list(card_pos.keys())
    candidates = list(permutations(keys))
    for candidate in candidates:
        temp = 0
        for num in candidate:
            pos1, pos2 = card_pos[num]
            result1_1 = bfs(board, r, c, pos1[0], pos1[1])
            result1_2 = bfs(board, pos1[0], pos1[1], pos2[0], pos2[1])
            result2_1 = bfs(board, r, c, pos2[0], pos2[1])
            result2_2 = bfs(board, pos2[0], pos2[1], pos1[0], pos1[1])
            result1 = result1_1 + result1_2
            result2 = result2_1 + result2_2
            if result1 < result2:
                temp += result1 + 2
                r, c = pos2
            else:
                temp += result2 + 2
                r, c = pos1
        answer = min(temp, answer)

    return answer


solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)
