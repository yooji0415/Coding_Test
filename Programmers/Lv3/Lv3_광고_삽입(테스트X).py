def solution(play_time, adv_time, logs):
    # 광고 시간과 영상 시간을 초로 환산한다
    adv_time_list = list(map(int, adv_time.split(":")))
    adv_time_sec = 3600 * adv_time_list[0] + 60 * adv_time_list[1] + adv_time_list[2]
    play_time_list = list(map(int, play_time.split(":")))
    play_time_sec = 3600 * play_time_list[0] + 60 * play_time_list[1] + play_time_list[2]

    # 로그 또한 초로 환산하다
    logs.sort()
    log_list = []
    for l in logs:
        start_end = l.split("-")
        start_time_list = list(map(int, start_end[0].split(":")))
        end_time_list = list(map(int, start_end[1].split(":")))
        start_time_sec = 3600 * start_time_list[0] + 60 * start_time_list[1] + start_time_list[2]
        end_time_sec = 3600 * end_time_list[0] + 60 * end_time_list[1] + end_time_list[2]
        log_list.append([start_time_sec, end_time_sec])

    # 로그의 시작 시간에서 광고 시간을 더했을때
    # 영상이 끝나는 시간을 넘는지 확인하고 그렇지 않은 경우만 리스트로 담는다
    candidate = []
    for l in log_list:
        if play_time_sec >= l[0] + adv_time_sec:
            candidate.append(l[0])
        else:
            break

    # 영상이 끝나기 전 광고 삽입 가능한 마지막 시간도 담는다
    candidate.append(play_time_sec - adv_time_sec)
    # print('find candidate complete : ', candidate)
    # print('log_list : ', log_list)

    # 후보군들을 돌면서 정답을 찾는다
    max_time = 0
    max_timing = 0
    for c in candidate:
        temp_time = 0
        c_start = c
        c_end = c + adv_time_sec
        for l in log_list:
            if l[0] <= c_start <= l[1] or l[0] <= c_end <= l[1]:
                temp_time += min(l[1], c_end) - max(c_start, l[0])

        if max_time < temp_time:
            max_time = temp_time
            max_timing = c

    # 정답을 찾았으면 해당 정답을 정리해서 리턴한다
    h = str(max_timing // 3600)
    m = str((max_timing % 3600) // 60)
    s = str((max_timing % 3600) % 60)
    answer = [h, m, s]
    for i in range(len(answer)):
        if len(answer[i]) == 1:
            answer[i] = '0' + answer[i]

    return ":".join(answer)


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))
