n, l = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def check(line):
    flag = True
    is_on = set()
    for x in range(1, n):
        if line[x] == line[x - 1]:
            continue
        if abs(line[x] - line[x - 1]) > 1:
            flag = False
            break
        if line[x] < line[x - 1]:
            now = line[x]
            if x + l - 1 >= n:
                flag = False
                break
            for nx in range(x, x + l):
                if line[nx] != now:
                    flag = False
                    break
                if nx in is_on:
                    flag = False
                    break
            if not flag:
                break
            else:
                for nx in range(x, x + l):
                    is_on.add(nx)

        else:
            now = line[x - 1]
            if x - l < 0:
                flag = False
                break
            for nx in range(x - l, x):
                if line[nx] != now:
                    flag = False
                    break
                if nx in is_on:
                    flag = False
                    break
            if not flag:
                break
            else:
                for nx in range(x - l, x):
                    is_on.add(nx)
    return flag


cnt = 0
# 가로부터 보자
for x in range(n):
    line = graph[x]
    if check(line):
        # print(f"가로: {x + 1}")
        cnt += 1

# 세로를 이제 보자
for x in range(n):
    line = []
    for y in range(n):
        line.append(graph[y][x])
    if check(line):
        # print(f"세로: {x + 1}")
        cnt += 1

print(cnt)

