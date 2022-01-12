def solution(sizes):
    answer = 0
    temp = 0
    for size in sizes:
        if size[0] >= size[1]:
            temp = size[0]
            size[0] = size[1]
            size[1] = temp

    max0 = 0
    max1 = 0
    for size in sizes:
        if max0 < size[0]:
            max0 = size[0]
        if max1 < size[1]:
            max1 = size[1]

    answer = max0 * max1
    return answer


# 모범답안
# 파이썬 내장함수를 이용한 간결한 풀이
def best_solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
