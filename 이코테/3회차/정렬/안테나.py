def solution(n, houses):
    houses.sort()
    print(houses[(n - 1) // 2])


print(solution(4, [5, 1, 7, 9]))
