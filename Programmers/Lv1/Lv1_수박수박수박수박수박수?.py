def solution(n):
    answer = ''
    alpha = ['수', '박']
    for i in range(n):
        answer += alpha[i % 2]

    return answer
