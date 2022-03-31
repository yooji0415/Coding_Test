def solution(n):
    answer = list(str(int(n)))
    answer = list(map(int, answer))
    answer.reverse()
    return answer
