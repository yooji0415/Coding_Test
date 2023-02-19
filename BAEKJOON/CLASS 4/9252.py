a = [0] + list(input())
b = [0] + list(input())

graph = [[0] * (len(a)) for _ in range(len(b))]

for y in range(len(b)):
    for x in range(len(a)):
        if y == 0 or x == 0:
            graph[y][x] = 0
        elif a[x] == b[y]:
            graph[y][x] = graph[y - 1][x - 1] + 1
        else:
            graph[y][x] = max(graph[y - 1][x], graph[y][x - 1])

# for line in graph:
#     print(line)

x = len(a) - 1
y = len(b) - 1
answer = []
while x > 0 and y > 0:
    now = graph[y][x]
    left = graph[y][x - 1]
    up = graph[y - 1][x]

    if up == now:
        y -= 1
        continue

    if left == now:
        x -= 1
        continue

    answer.append(a[x])
    x -= 1
    y -= 1

answer.reverse()
print(graph[len(b) - 1][len(a) - 1])
print("".join(map(str, answer)))
