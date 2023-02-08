def solution(k, d):
    points = 0
    for x in range(0, d + 1, k):
        y_max = (d ** 2 - x ** 2) ** 0.5
        points += y_max // k + 1

    return points