def solution(numbers):
    answer = []
    s_numbers = sorted(numbers)
    for i in range(1, len(s_numbers)):
        for j in range(0, i):
            sum = s_numbers[i] + s_numbers[j]
            if sum not in answer:
                answer.append(sum)

    answer = sorted(answer)
    return answer


# 모범답안
# 좀 더 간결하게 표현한 느낌이다.
def best_solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
