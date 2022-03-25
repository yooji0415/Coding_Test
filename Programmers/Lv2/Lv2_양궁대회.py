# -*- coding: utf-8 -*-
from itertools import combinations_with_replacement as combi


def solution(n, info):
    # 점수 (10 점 부터 0 점 까지) 기입해 둔 list
    s_list = [i for i in range(11)]

    # 중복 조합을 한 결과를 list 로 받는다
    combi_result = list(combi(s_list, n))

    # 각 list 에서 count 를 해서 넣는다
    s_result = []
    for result in combi_result:
        temp = [0] * 11
        for s in result:
            temp[10 - s] += 1

        s_result.append(temp)

    # 어피치 와 비교후 점수 계산
    best_list = []
    best_score = 0
    for result in s_result:
        li_score = 0
        ap_score = 0
        # 점수 계산
        for i in range(11):
            # 둘 다 0일 경우를 제외
            if info[i] == 0 and result[i] == 0:
                continue
            # 라이언 이 점수를 가져갈 때
            if info[i] < result[i]:
                li_score += (10 - i)
            else:
                ap_score += (10 - i)

        # 결과 확인
        if best_score < li_score - ap_score:
            best_score = li_score - ap_score
            best_list = result

    if best_score == 0:
        return [-1]
    else:
        return best_list

