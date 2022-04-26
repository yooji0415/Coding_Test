def solution(s):
    answer = ''
    s_len = len(s)
    if s_len in [1, 2]:
        return s

    if s_len % 2 == 0:
        return s[s_len // 2 - 1:s_len // 2 + 1]
    else:
        return s[s_len // 2]
