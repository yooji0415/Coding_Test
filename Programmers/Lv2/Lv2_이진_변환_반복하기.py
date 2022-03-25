def solution(s):
    cnt = 0
    r_zero = 0
    while s != "1":
        i_len = len(s)
        s = s.replace("0", "")
        o_len = len(s)
        r_zero += i_len - o_len
        s = bin(int(o_len))[2:]
        cnt += 1
    return [cnt, r_zero]

