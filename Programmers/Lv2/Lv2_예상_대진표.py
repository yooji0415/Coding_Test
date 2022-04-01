def solution(n, a, b):
    answer = 0
    if b < a:
        a, b = b, a

    cnt = 1
    while (b - a) > 0:
        if ((b - 1) // 2) == ((a - 1) // 2):
            break

        if a % 2 == 1:
            a += 1
        if b % 2 == 1:
            b += 1

        a //= 2
        b //= 2

        cnt += 1

    return cnt