import math


def solution(n, k):
    n_list = [x for x in range(1, n + 1)]
    answer = []
    while n != 0:
        # 현 자리에서 뒤에 올 경우의 수를 temp에 저장
        temp = math.factorial(n - 1)
        # 인덱스가 0부터이니 k - 1에서 temp만큼 나누고 나온 몫이
        # 현 위치에 들어갈 숫자
        i, k = (k - 1) // temp, k % temp
        answer.append(n_list.pop(i))
        n -= 1

    return answer