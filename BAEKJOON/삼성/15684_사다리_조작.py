import sys

input = sys.stdin.readline

N, M, H = map(int, input().split())

lines = [[False] * (N - 1) for _ in range(H)]
answer = 4

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    lines[a][b] = True


def check():
    for i in range(N):
        x, y = i, 0
        while y < H:
            if x == N - 1:
                if lines[y][x - 1]:
                    x -= 1
            elif x == 0:
                if lines[y][x]:
                    x += 1
            else:
                if lines[y][x]:
                    x += 1

                elif lines[y][x - 1]:
                    x -= 1
            y += 1

        if x != i:
            return False

    return True


def back_tracking(cnt, last_x, last_y):
    global answer
    if cnt > answer or cnt > 3:
        return

    if check():
        answer = cnt if answer > cnt else answer

    for y in range(last_y, H):
        for x in range(N - 1):
            if y == last_y and x < last_x:
                continue

            if not lines[y][x]:
                if x == 0:
                    if lines[y][x + 1]:
                        continue
                elif x == N - 2:
                    if lines[y][x - 1]:
                        continue
                else:
                    if lines[y][x + 1] or lines[y][x - 1]:
                        continue

                lines[y][x] = True
                back_tracking(cnt + 1, x, y)
                lines[y][x] = False

    return


back_tracking(0, 0, 0)

if answer > 3:
    answer = -1
print(answer)
