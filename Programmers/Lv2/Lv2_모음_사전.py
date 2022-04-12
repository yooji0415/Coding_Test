def solution(word):
    answer = 0
    # 글자를 순서대로 적어보면 각 자리수 마다의 간격이 있다
    # 해당 간격을 이용한 풀이법
    w = ['A', 'E', 'I', 'O', 'U']
    d = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        alpha = word[i]
        idx = w.index(alpha)
        answer += idx * d[i] + 1
    return answer
