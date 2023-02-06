import sys

sys.setrecursionlimit(10 ** 7)


def check_fun(word):
    cnt = 0
    for w in word:
        if w == "(":
            cnt += 1
            continue
        if cnt == 0:
            return False
        cnt -= 1

    if cnt == 0:
        return True
    return False


def solution(p):
    # 빈 문자열인 경우 리턴
    if p == "":
        return p
    # 완벽한 문자열이면 리턴
    if check_fun(p):
        return p
    # u를 분리한다.
    start_cnt = 0
    end_cnt = 0
    u = ""
    for w in p:
        if w == "(":
            start_cnt += 1
            u += "("
        else:
            u += ")"
            end_cnt += 1

        if start_cnt == end_cnt:
            break
    v = ''
    if len(u) != len(p):
        v = p[len(u):]
    # v에 대해서 재귀
    v = solution(v)
    # u가 올바르다면
    if check_fun(u):
        return u + v
    # u가 올바르지 않으면
    answer = "(" + v + ")"
    u = list(u)[1:]
    u.pop()
    for w in u:
        if w == "(":
            answer += ")"
        else:
            answer += "("
    return answer
