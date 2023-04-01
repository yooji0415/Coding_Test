def check(cols, rows):
    for col in cols:
        x, y, _ = col
        if y == 0:
            continue
        flag = False
        for other_col in cols:
            ox, oy, _ = other_col
            if ox == x and oy == y - 1:
                flag = True
                break
        if flag:
            continue
        for row in rows:
            rx, ry, _ = row
            if ry == y and (rx == x or rx == x - 1):
                flag = True
                break
        if not flag:
            return False

    for row in rows:
        x, y, _ = row
        flag = False
        for col in cols:
            cx, cy, _ = col
            if (cx == x and cy == y - 1) or (cx == x + 1 and cy == y - 1):
                flag = True
                break
        if flag:
            continue
        left = False
        right = False
        for other_row in rows:
            ox, oy, _ = other_row
            if y == oy:
                if x - 1 == ox:
                    left = True
                if x + 1 == ox:
                    right = True
        if not left or not right:
            return False

    return True


def solution(n, build_frame):
    cols = []
    rows = []
    for build in build_frame:
        x, y, a, b = build
        if b == 1:
            if a == 0:
                cols.append((x, y, a))
                if not check(cols, rows):
                    cols.pop()
            else:
                rows.append((x, y, a))
                if not check(cols, rows):
                    rows.pop()
        else:
            if a == 0:
                target = (x, y, a)
                cols.remove(target)
                if not check(cols, rows):
                    cols.append(target)
            else:
                target = (x, y, a)
                rows.remove(target)
                if not check(cols, rows):
                    rows.append(target)

    answer = cols + rows
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
