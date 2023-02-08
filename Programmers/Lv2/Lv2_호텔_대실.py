def time_to_min(hour, minute):
    return hour * 60 + minute


def solution(book_time):
    answer = 0
    min_list = []

    for [start_time, end_time] in book_time:
        start_hour, start_minute = map(int, start_time.split(":"))
        end_hour, end_minute = map(int, end_time.split(":"))
        min_list.append((time_to_min(start_hour, start_minute), time_to_min(end_hour, end_minute)))

    min_list.sort()
    # print(min_list)

    for i in range(len(min_list)):
        cnt = 0
        cur_start = min_list[i][0]
        for j in range(0, i):
            if cur_start - 10 < min_list[j][1]:
                cnt += 1

        answer = max(answer, cnt + 1)

    return answer
