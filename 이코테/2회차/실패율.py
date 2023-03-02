def solution(N, stages):
    answer = []
    arr = [0 for _ in range(N + 2)]

    for stage in stages:
        arr[stage] += 1

    result = []
    length = len(stages)

    for i in range(1, N + 1):
        if length == 0:
            result.append((i, 0))
            continue
        result.append((i, arr[i] / length))
        length -= arr[i]

    result.sort(key=lambda x: (-x[1], x[0]))

    for i in result:
        answer.append(i[0])

    return answer
