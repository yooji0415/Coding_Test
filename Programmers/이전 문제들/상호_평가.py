def solution(scores):
    students = []
    for y in range(len(scores)):
        max_val = -int(1e9)
        max_idx = 0
        min_val = int(1e9)
        min_idx = 0
        total = 0
        for x in range(len(scores)):
            score = scores[x][y]
            total += score
            if score > max_val:
                max_val = score
                max_idx = x
            elif score < min_val:
                min_val = score
                min_idx = x
        average = 0
        if max_idx == y:
            total -= max_val
            average = total / (len(scores) - 1)
        elif min_idx == y:
            total -= min_val
            average = total / (len(scores) - 1)
        else:
            average = total / len(scores)
        # 이제 학점 부여
        if average >= 90:
            students.append("A")
        elif average >= 80:
            students.append("B")
        elif average >= 70:
            students.append("C")
        elif average >= 50:
            students.append("D")
        else:
            students.append("F")

    return "".join(students)


print(solution(
    [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))

