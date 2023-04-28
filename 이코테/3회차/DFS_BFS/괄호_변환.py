def solution(word):
    # 1
    if not word:
        return word
    # 2 3
    cnt = 0
    end_point = 0
    is_correct = True
    for i in range(len(word)):
        if word[i] == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            is_correct = False

        if cnt == 0:
            end_point = i
            break
    # 3 - 1
    if is_correct:
        return word[:end_point + 1] + solution(word[end_point + 1:])
    # 4
    result = "(" + solution(word[end_point + 1:]) + ")"
    u = word[1:end_point]
    for w in u:
        if w == "(":
            result += ")"
        else:
            result += "("
    return result


print(solution(""))
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
