# -*- coding: utf-8 -*-
import math


def is_prime_num(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    # 먼저 k 진수로 바꿔준다
    k_num = ""
    while n > k:
        temp = n % k
        k_num = str(temp) + k_num
        n = n // k
    k_num = str(n) + k_num

    # 이후 stack 을 활용해서 소수 후보군을 뽑아낸다
    nums = []
    temp = ""
    for i in range(len(k_num)):
        # 0 을 만난 경우에 temp 에 있던 수를 넣어준다
        if k_num[i] == "0":
            if temp != "":
                nums.append(int(temp))
                temp = ""
        else:
            temp += k_num[i]
    # 반복문을 빠져나온 이후 temp가 남아있으면 추가해준다
    if temp != "":
        nums.append(int(temp))

    # 후보군들 중에서 소수의 개수를 찾는다
    cnt = 0
    for n in nums:
        if n < 2:
            continue

        if is_prime_num(n):
            cnt += 1

    return cnt

