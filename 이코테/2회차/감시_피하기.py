N = int(input())
graph = []
teachers = []

for y in range(N):
    arr = input().split()
    graph.append(arr)
    for x in range(len(arr)):
        if arr[x] == "T":
            # 선생님의 위치를 y, x 로 담는다.
            teachers.append((y, x))


def check_teacher():
    for teacher in teachers:
        flag = False
        t_y, t_x = teacher
        # 오른쪽
        for x in range(t_x + 1, N):
            if graph[t_y][x] == "O":
                break
            if graph[t_y][x] == "S":
                flag = True
                break
        if flag:
            return False
        # 왼쪽
        for x in range(t_x - 1, -1, -1):
            if graph[t_y][x] == "O":
                break
            if graph[t_y][x] == "S":
                flag = True
                break
        if flag:
            return False
        # 위
        for y in range(t_y - 1, -1, -1):
            if graph[y][t_x] == "O":
                break
            if graph[y][t_x] == "S":
                flag = True
                break
        if flag:
            return False
        # 아래
        for y in range(t_y + 1, N):
            if graph[y][t_x] == "O":
                break
            if graph[y][t_x] == "S":
                flag = True
                break
        if flag:
            return False

    return True


def dfs(cnt):
    if cnt >= 3:
        return check_teacher()

    for y in range(N):
        for x in range(N):
            if graph[y][x] == "X":
                graph[y][x] = "O"
                if dfs(cnt + 1):
                    return True
                graph[y][x] = "X"

    return False


answer = dfs(0)
print("YES" if answer else "NO")
