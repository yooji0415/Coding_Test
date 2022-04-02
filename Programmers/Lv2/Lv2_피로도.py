from itertools import permutations


def solution(k, dungeons):
    answer_list = []
    for case in permutations(dungeons, len(dungeons)):
        cnt = 0
        temp = k
        for i in range(len(case)):
            if case[i][0] <= temp:
                temp -= case[i][1]
                cnt += 1
                if temp <= 0:
                    break

        answer_list.append(cnt)

    return max(answer_list)

