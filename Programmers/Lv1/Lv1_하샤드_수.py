def solution(x):
    answer = True
    str_x = str(x)
    div = 0
    for i in range(len(str_x)):
        div += int(str_x[i])

    if x % div != 0:
        answer = False
    return answer