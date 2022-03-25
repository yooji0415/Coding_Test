# -*- coding: utf-8 -*-
def solution(id_list, report, k):
    # 1. 신고를 받은 사람에게 신고자를 넣어준다
    # 2. 신고 수가  k개를 넘은 인원을 찾는다
    # 3. 해당 인원을 신고한 신고자의 카운트를 올린다
    # 1.
    member = {}
    r_cnt = {}
    for i in range(len(id_list)):
        member[id_list[i]] = i
        r_cnt[i] = []

    for r in report:
        id = r.split()
        if member[id[0]] not in r_cnt[member[id[1]]]:
            r_cnt[member[id[1]]].append(member[id[0]])

    # 2.
    # 3.
    answer = [0] * len(id_list)
    for i in r_cnt.keys():
        if len(r_cnt[i]) >= k:
            for j in r_cnt[i]:
                answer[j] += 1

    return answer


# 모범답안
# 동일 아이디어지만 파이썬에 대한 이해도 차이로
# 코드의 간결성에서 차이가 난다
def best_solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

