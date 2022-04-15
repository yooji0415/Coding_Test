def time_to_sec(time):
    time_list = list(map(int, time.split(":")))
    sec = 3600 * time_list[0] + 60 * time_list[1] + time_list[2]
    return sec


def solution(play_time, adv_time, logs):
    # 광고 시간과 영상 시간을 초로 환산한다
    adv_time_sec = time_to_sec(adv_time)
    play_time_sec = time_to_sec(play_time)

    # 로그 또한 초로 환산하다
    # 전체 초 만큼의 list를 만들고 해당 list를 누적 값으로 바꾼다
    time_list = [0] * (play_time_sec + 1)
    start_list = []
    end_list = []
    for l in logs:
        start_end = l.split("-")
        start_time_sec = time_to_sec(start_end[0])
        end_time_sec = time_to_sec(start_end[1])
        time_list[start_time_sec] += 1
        time_list[end_time_sec] -= 1

    for i in range(1, len(time_list)):
        time_list[i] += time_list[i - 1]

    for i in range(1, len(time_list)):
        time_list[i] += time_list[i - 1]

    # 누적 값을 이용해서 가장 많은 동시 시청 시간을 알아낸다
    max_value = 0
    max_time = 0
    for i in range(adv_time_sec - 1, play_time_sec):
        if i == adv_time_sec - 1:
            if time_list[i] > max_value:
                max_value = time_list[i]
                max_time = i - adv_time_sec + 1
        if time_list[i] - time_list[i - adv_time_sec] > max_value:
            max_value = time_list[i] - time_list[i - adv_time_sec]
            max_time = i - adv_time_sec + 1

    # 정답을 찾았으면 해당 정답을 정리해서 리턴한다
    h = max_time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    max_time = max_time % 3600
    m = max_time // 60
    m = '0' + str(m) if m < 10 else str(m)
    max_time = max_time % 60
    s = '0' + str(max_time) if max_time < 10 else str(max_time)
    return h + ':' + m + ':' + s


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
