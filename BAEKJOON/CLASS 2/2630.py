import sys

input = sys.stdin.readline

n = int(input())
graph = []
answer_one = 0
answer_zero = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))


# n은 2의 승수 / x, y 는 시작 포인트
def check_one_zero(n, x, y):
    global answer_one
    global answer_zero
    # 만약 0이면
    if n == 0:
        if graph[y][x] == 1:
            answer_one += 1
        else:
            answer_zero += 1
        return

    length = 2 ** n
    end_x = x + length
    end_y = y + length

    flag_one = True
    flag_zero = True
    for nx in range(x, end_x):
        for ny in range(y, end_y):
            if flag_one and graph[ny][nx] == 0:
                flag_one = False
            elif flag_zero and graph[ny][nx] == 1:
                flag_zero = False

            if not flag_zero and not flag_one:
                break

        if not flag_zero and not flag_one:
            break

    if flag_zero:
        answer_zero += 1
        return

    if flag_one:
        answer_one += 1
        return

    check_one_zero(n - 1, x, y)
    check_one_zero(n - 1, x + 2 ** (n - 1), y)
    check_one_zero(n - 1, x, y + 2 ** (n - 1))
    check_one_zero(n - 1, x + 2 ** (n - 1), y + 2 ** (n - 1))


num = 0
while n > 1:
    num += 1
    n //= 2

check_one_zero(num, 0, 0)
print(answer_zero)
print(answer_one)
