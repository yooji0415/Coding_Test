n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0


def check_max(x, y, sum):
    if y == 0:
        return sum

    result_x = 0
    result = 0
    for nx in [x - 1, x]:
        if nx < 0 or nx > y - 1:
            continue
        if result < sum + graph[y - 1][nx]:
            result = sum + graph[y - 1][nx]
            result_x = nx

    return check_max(result_x, y - 1, result)


for i in range(n):
    answer = max(answer, check_max(i, n - 1, graph[n - 1][i]))

print(answer)
