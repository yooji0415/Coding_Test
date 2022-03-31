def solution(s):
    answer = ''
    cnt = 1
    for i in range(len(s)):
        if s[i].isalpha():
            if cnt % 2 == 0:
                answer += s[i].lower()
                cnt += 1
            else:
                answer += s[i].upper()
                cnt += 1
        else:
            answer += s[i]
            cnt = 1

    return answer
