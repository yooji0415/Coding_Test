def time_to_ms(time):
    day, end_time, spend_time = time.split()
    hour, minute, sec = end_time.split(":")
    end_time_ms = 60 * 60 * 1000 * int(hour) + 60 * 1000 * int(minute) + int(1000 * float(sec))
    start_time_ms = end_time_ms - int(1000 * float(spend_time[:-1])) + 1
    print(start_time_ms, end_time_ms)
    return [start_time_ms, end_time_ms]


def solution(lines):
    answer = 0
    timeline = []
    for line in lines:
        timeline.append(time_to_ms(line))

    for i in range(len(lines)):
        cnt = 0
        cur_end_time = timeline[i][1]
        for j in range(i, len(lines)):
            if cur_end_time > timeline[j][0] - 1000:
                cnt += 1
        answer = max(answer, cnt)

    return answer

