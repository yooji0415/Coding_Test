n = int(input())
graph = [[" "] * n for _ in range(n)]


def print_star(x, y, length):
    global graph
    if length == 3:
        d = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            graph[nx][ny] = "*"
        return

    new_length = length // 3

    print_star(x, y, new_length)
    print_star(x, y + new_length, new_length)
    print_star(x, y + new_length * 2, new_length)
    print_star(x + new_length, y, new_length)
    print_star(x + new_length, y + new_length * 2, new_length)
    print_star(x + new_length * 2, y, new_length)
    print_star(x + new_length * 2, y + new_length, new_length)
    print_star(x + new_length * 2, y + new_length * 2, new_length)


print_star(0, 0, n)
for line in graph:
    print("".join(line))
