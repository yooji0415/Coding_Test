def solution(rows, columns, queries):
    table = []
    answer = []
    for i in range(rows):
        table.append([x for x in range(1 + columns * i, 1 + columns * (i + 1))])

    for r in queries:
        y1, x1, y2, x2 = r[0] - 1, r[1] - 1, r[2] - 1, r[3] - 1
        temp = table[y1][x1]
        min_num = temp

        # 왼쪽
        for y in range(y1, y2):
            min_num = min(min_num, table[y][x1])
            table[y][x1] = table[y + 1][x1]
        # 아래
        for x in range(x1, x2):
            min_num = min(min_num, table[y2][x])
            table[y2][x] = table[y2][x + 1]
        # 오른쪽
        for y in range(y2, y1, -1):
            min_num = min(min_num, table[y][x2])
            table[y][x2] = table[y - 1][x2]
        # 위
        for x in range(x2, x1, -1):
            min_num = min(min_num, table[y1][x])
            table[y1][x] = table[y1][x - 1]

        table[y1][x1 + 1] = temp
        answer.append(min_num)

    return answer

