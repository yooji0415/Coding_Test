def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)
    scores.sort(key=lambda s: (-s[0], s[1]))
    print(scores)
    max_company, answer = 0, 1
    for s in scores:
        # 완호 점수보다 둘 다 잘 나온경우 리턴이다.
        if wanho[0] < s[0] and wanho[1] < s[1]:
            return -1
        # 2번째 점수가 지금 맥스보다 높거나 같으면
        if max_company <= s[1]:
            # 일단 완호의 합과 비교하고 더 크면
            if wanho_sum < s[0] + s[1]:
                # 앞 등수를 내어준다.
                answer += 1
            # 2번째 점수 맥스를 바꿔준다.
            max_company = s[1]
    return answer


print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))
