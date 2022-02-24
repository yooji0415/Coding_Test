def solution(n):
    temp = n + 1
    s_cnt = bin(n)[2:].count("1")
    while True:
        b = bin(temp)[2:]
        if b.count("1") == s_cnt:
            return temp
        else:
            temp += 1

            