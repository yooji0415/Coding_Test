import sys


def check(num):
    # 모두 num 으로 바꾸는 경우를 계산
    # flag가 True인 경우는 연속된 라인을 찾는 중
    flag = False
    cnt = 0
    for i in range(len(s)):
        if s[i] != num:
            if not flag:
                flag = True
        else:
            if flag:
                cnt += 1
                flag = False

    if flag:
        cnt += 1

    return cnt


s = sys.stdin.readline().strip()
print(min(check('0'), check('1')))
