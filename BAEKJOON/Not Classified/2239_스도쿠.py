import sys

input = sys.stdin.readline

graph = []
blanks = []

for x in range(9):
    line = list(map(int, list(input().strip())))
    for y in range(9):
        if line[y] == 0:
            blanks.append((x, y))
    graph.append(line)


def check(graph, x, y, val):
    # 가로
    for i in range(9):
        if val == graph[x][i]:
            return False
    # 세로
    for i in range(9):
        if val == graph[i][y]:
            return False
    # 정방 칸
    row = x // 3 * 3
    col = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if val == graph[row + i][col + j]:
                return False
    return True


def dfs(idx, graph, blanks):
    if idx == len(blanks):
        for line in graph:
            print("".join(list(map(str, line))))
        sys.exit(0)

    for i in range(1, 10):
        x, y = blanks[idx]
        if check(graph, x, y, i):
            graph[x][y] = i
            dfs(idx + 1, graph, blanks)
            graph[x][y] = 0


dfs(0, graph, blanks)
