def check_possible(answer):
    for build in answer:
        x, y, _type = build
        # 기둥인 경우
        if _type == 0:
            if y == 0 or [x, y, 1] in answer or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        # 보인 경우
        else:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    # n 은 격자다 0 ~ n 까지의 격자
    # build_frame 은 무엇인가
    # x: 시작점 위치 y: 시작점 위치 a: 0 기둥 1 보 b: 0 삭제 1 설치
    for build in build_frame:
        x, y, _type, is_build = build
        if is_build == 1:
            answer.append([x, y, _type])
            if check_possible(answer):
                continue
            answer.pop()
        else:
            answer.remove([x, y, _type])
            if check_possible(answer):
                continue
            answer.append([x, y, _type])

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))
