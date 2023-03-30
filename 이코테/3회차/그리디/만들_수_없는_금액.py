def solution(n, array):
    array.sort()
    answer = 1
    for num in array:
        if answer < num:
            return answer
        answer += num


print(solution(5, [3, 2, 1, 1, 9]))
