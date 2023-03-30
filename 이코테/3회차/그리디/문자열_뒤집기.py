def solution(num_str):
    zero_cnt = 0
    one_cnt = 0
    array = list(map(int, list(num_str)))
    now = array[0]
    for num in array:
        if now != num:
            if now == 1:
                one_cnt += 1
            else:
                zero_cnt += 1
            now = num
    return min(zero_cnt, one_cnt)


print(solution("0001100"))
print(solution("010110000"))
