def solution(line):
    stars = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            # 두 직선이 평행인 경우만 아니면 교점은 있다.
            if a * d - b * c != 0:
                x, y = (b * f - e * d) / (a * d - b * c), (e * c - a * f) / (a * d - b * c)
                if x.is_integer() and y.is_integer():
                    x, y = int(x), int(y)
                    if (x, y) not in stars:
                        stars.append((x, y))

    x_min, x_max, y_min, y_max = min(stars)[0], max(stars)[0], min(stars, key=lambda x: x[1])[1], \
                                 max(stars, key=lambda x: x[1])[1]
    answer = [['.'] * (abs(x_max - x_min) + 1) for _ in range((abs(y_max - y_min) + 1))]
    for star in stars:
        a, b = star
        x, y = abs(x_min - a), abs(y_max - b)
        answer[y][x] = '*'
    for i, v in enumerate(answer):
        answer[i] = ''.join(v)
    return answer
