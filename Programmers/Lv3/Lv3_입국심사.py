def solution(n, times):
    answer = 0
    max_time = max(times) * n;
    min_time = 0

    while min_time <= max_time:
        mid_time = (max_time + min_time) // 2
        cnt = 0
        for time in times:
            cnt += mid_time // time
            if cnt >= n:
                break

        if cnt >= n:
            max_time = mid_time - 1
            answer = mid_time

        else:
            min_time = mid_time + 1

    return answer