def solution(d, budget):
    answer = 0
    s_d = sorted(d)
    for item in s_d:
        if budget - item >= 0:
            answer += 1
            budget -= item

    return answer


# 모범답안
# 큰 값 부터 제외하는게 더 성능이 빠를 것이다.
def best_solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
