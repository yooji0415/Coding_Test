def solution(N, stages):
    try_array = [0] * (2 + N)
    for stage in stages:
        try_array[stage] += 1
    total = len(stages)
    fail_rates = []
    for i in range(1, N + 1):
        if total > 0:
            fail_rates.append((try_array[i] / total, i))
        else:
            fail_rates.append((0, i))
        total -= try_array[i]
    fail_rates.sort(key=lambda x: (-x[0], x[1]))
    return [x[1] for x in fail_rates]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(5, [4, 4, 4, 4, 4]))
