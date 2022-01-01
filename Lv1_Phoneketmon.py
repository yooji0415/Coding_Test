import numpy


def solution(nums):
    answer = 0
    unq = numpy.unique(nums)
    select_num = len(nums) / 2
    if len(unq) < select_num:
        answer = len(unq)
    else:
        answer = select_num

    return answer


# 모범답안
def best_solution(ls):
    # set 함수를 이용한 중복제거 아이디어를 생각해보지 못했다.
    return min(len(ls)/2, len(set(ls)))
