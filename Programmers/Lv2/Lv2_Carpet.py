import math


def solution(brown, yellow):
    test_list = []
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            test_list.append([i, yellow // i])

    answer = []
    for t in test_list:
        if 2 * (t[0] + t[1] + 4) - 4 == brown:
            answer = [t[0] + 2, t[1] + 2]
            break

    answer.sort(reverse=True)
    return answer
