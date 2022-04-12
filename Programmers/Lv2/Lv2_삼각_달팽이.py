def solution(n):
    answer = [[0 for j in range(1, i + 1)] for i in range(1, n + 1)]

    y = -1
    x = 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            else:
                y -= 1
                x -= 1
            answer[y][x] = num
            num += 1
            # print(answer)

    return sum(answer, [])


# print(solution(3))
