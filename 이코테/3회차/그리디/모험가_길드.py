import sys

input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))


def solution(n, array):
    answer = 0
    array.sort()
    cnt = 0
    max_num = 0
    for num in array:
        max_num = max(num, max_num)
        cnt += 1
        if cnt >= max_num:
            answer += 1
            cnt = 0
            max_num = 0
    return answer


print(solution(n, array))
