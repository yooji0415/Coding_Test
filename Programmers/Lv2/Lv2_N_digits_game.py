# -*- coding: utf-8 -*-
def solution(n, t, m, p):
    answer = ''
    # 순서 고려 없이 100000 까지의 숫자를 n 진법에 맞춰서 숫자를 나열한다
    num = 100000
    num_list = '0'
    setting = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(1, num):
        n_num = ''
        while i >= n:
            temp = i % n
            n_num = setting[temp] + n_num
            i //= n
        n_num = setting[i] + n_num
        num_list += n_num

    # 튜브의 순서를 고려해서 숫자를 추가한다
    for j in range(t):
        answer += num_list[j * m + p - 1]

    return answer

