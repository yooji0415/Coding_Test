def solution(n, s):
    answer = []
    while n > 0:
        temp = s // n
        if temp == 0:
            return [-1]
        answer.append(temp)
        s -= temp
        n -= 1

    answer.sort()
    return answer