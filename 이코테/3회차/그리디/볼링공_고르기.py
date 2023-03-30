def solution(n, m, array):
    _set = set(array)
    _dict = {i: 0 for i in _set}
    for num in array:
        _dict[num] += 1
        
    total = len(array)
    answer = 0
    for num in _set:
        total -= _dict[num]
        answer += total * _dict[num]
    return answer


print(solution(5, 3, [1, 3, 2, 3, 2]))
print(solution(8, 5, [1, 5, 4, 3, 2, 4, 5, 2]))
