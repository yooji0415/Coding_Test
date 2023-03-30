import sys

input = sys.stdin.readline
num = input().strip()


def solution(num_str):
    num_list = list(map(int, list(num_str)))
    answer = num_list[0]
    for num in num_list[1:]:
        if answer == 0:
            answer += num
            continue
        answer *= num
    return answer


print(solution(num))
