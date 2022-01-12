def solution(N, stages):
    stage_count = []
    failure_rate = {}
    player_num = len(stages)
    # 스테이지 마다 몇명이 있는지 확인
    for i in range(1, N + 1):
        stage_count.append(stages.count(i))

    # 스테이지 별 실패율 계산 완료
    for j in range(1, N + 1):
        if player_num == 0:
            failure_rate[j] = 0
        else:
            failure_rate[j] = stage_count[j-1] / player_num
            player_num -= stage_count[j-1]

    # 값 기준으로 정렬
    s_failure_rate = sorted(failure_rate, key=lambda x: failure_rate[x], reverse=True)

    return s_failure_rate


# 모범답안
# 위 내용을 다듬어서 깔끔하게 정리한 코드이다.
# 카운트 어레이 작업 없이 한 번에 안에서 돌게 한 점이 포인트다.
def best_solution(N, stages):
    fail_rate = {}
    total_user = len(stages)

    for stage in range(1, N+1):
        if total_user != 0:
            fail_user = stages.count(stage)
            fail_rate[stage] = fail_user / total_user
            total_user -= fail_user
        else:
            fail_rate[stage] = 0

    return sorted(fail_rate, key=lambda x : fail_rate[x], reverse=True)