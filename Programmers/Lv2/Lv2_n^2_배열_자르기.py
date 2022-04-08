def solution(n, left, right):
    answer = []
    for i in range(int(left), int(right + 1)):
        row = i // n
        col = i % n
        if row >= col:
            answer.append(row + 1)
        else:
            answer.append(col + 1)

    return answer