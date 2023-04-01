def solution(string):
    str_answer = []
    num_answer = 0
    for alpha in string:
        if alpha.isdigit():
            num_answer += int(alpha)
        else:
            str_answer.append(alpha)
    str_answer.sort()
    return "".join(str_answer) + str(num_answer)


print(solution("K1KA5CB7"))
print(solution("AJKDLSI412K4JSJ9D"))
