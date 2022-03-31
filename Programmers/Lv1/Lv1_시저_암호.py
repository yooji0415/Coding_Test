def solution(s, n):
    u = [chr(x) for x in range(65, 91)]
    l = [chr(x) for x in range(97, 123)]

    answer = ''
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                idx = u.index(s[i])
                idx += n
                answer += u[idx % 26]
            else:
                idx = l.index(s[i])
                idx += n
                answer += l[idx % 26]
        else:
            answer += s[i]

    return answer
