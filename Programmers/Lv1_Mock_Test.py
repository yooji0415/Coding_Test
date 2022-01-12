def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(answers)):
        if answers[i] == supo1[i % 5]:
            cnt1 += 1
        if answers[i] == supo2[i % 8]:
            cnt2 += 1
        if answers[i] == supo3[i % 10]:
            cnt3 += 1

    best = max(cnt1, cnt2, cnt3)
    if cnt1 == best:
        answer.append(1)
    if cnt2 == best:
        answer.append(2)
    if cnt3 == best:
        answer.append(3)
    return answer


# 모범답안
# enumerate 를 활용한 간결한 풀이
def best_solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
