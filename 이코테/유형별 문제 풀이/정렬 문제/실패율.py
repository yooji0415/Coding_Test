def solution(N, stages):
    result = []
    # 실패율 = 스테이지에 도달했으나 아직 클리어 못한 수 / 도달 한 사람 수
    stages_list = [0] * (N + 2)
    for stage in stages:
        stages_list[stage] += 1

    cnt = len(stages)
    for i in range(1, N + 1):
        if cnt == 0:
            result.append((0, i))
            continue
        result.append((stages_list[i] / cnt, i))
        cnt -= stages_list[i]

    result.sort(key=lambda x: (-x[0], x[1]))
    answer = []
    for r in result:
        answer.append(r[1])

    return answer
