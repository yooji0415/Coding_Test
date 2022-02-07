def solution(s):
    answer = 0
    for i in range(len(s)):
        if s[i] == '(':
            answer += 1
        elif s[i] == ')':
            answer += -1

        if answer < 0:
            return False

    if answer == 0:
        return True
    else:
        return False
