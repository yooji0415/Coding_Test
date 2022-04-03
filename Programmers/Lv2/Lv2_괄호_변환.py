def solution(p):
    # 1. 빈 문자열
    if len(p) == 0:
        return ''
    # 2. 균형 잡힌 괄호 문자열
    cnt = 0
    zero_point = 0
    is_correct = True
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                is_correct = False

        if cnt == 0:
            zero_point = i
            break

    u = p[:zero_point + 1]
    v = p[zero_point + 1:]
    # 3. 올바른 괄호 문자열
    if is_correct:
        answer = u + solution(v)
        return answer
    # 4. 아닌 경우
    u = u[1:-1]
    temp = ''
    for j in range(len(u)):
        if u[j] == '(':
            temp = temp + ')'
        else:
            temp = temp + '('
    answer = '(' + solution(v) + ')' + temp
    return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
