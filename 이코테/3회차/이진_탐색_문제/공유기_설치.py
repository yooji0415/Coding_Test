def solution(N, C, houses):
    houses.sort()
    left = 1
    right = houses[-1]
    answer = 1
    while left <= right:
        mid = (left + right) // 2
        cnt = 1
        now = houses[0]
        for i in range(len(houses)):
            if houses[i] < now + mid:
                continue
            cnt += 1
            now = houses[i]
        if cnt >= C:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    return answer


print(solution(5, 3, [1, 2, 8, 4, 9]))
