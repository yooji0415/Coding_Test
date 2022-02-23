def solution(numbers):
    s = list(map(str, numbers))
    s.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(s)))
    return answer