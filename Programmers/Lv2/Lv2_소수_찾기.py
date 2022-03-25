from itertools import permutations
import math


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    n_list = list(numbers)
    for i in range(1, len(n_list) + 1):
        p_list = permutations(n_list, i)
        for p in p_list:
            temp = int("".join(p))
            if temp not in [0, 1] and is_prime_number(temp) and temp not in answer:
                answer.append(temp)

    return len(answer)

