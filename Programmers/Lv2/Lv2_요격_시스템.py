def solution(targets):
    answer = 1
    targets.sort(key=lambda x:x[1])
    now_end = targets[0][1]
    for target in targets[1:]:
        if target[0] >= now_end:
            answer += 1
            now_end = target[1]
    return answer