# -*- coding: utf-8 -*-
def solution(fees, records):
    # 우선 입출차 내역을 정리한다
    parking = {}
    for r in records:
        info = r.split()
        time = info[0]
        car_num = info[1]
        if car_num not in parking:
            parking[car_num] = [time]
        else:
            parking[car_num].append(time)

    # 추차요금을 계산한다
    total = []
    for key, value in parking.items():
        # 시간을 우선적으로 계산한다
        # 홀수개의 시간이 저장됬다는 것은 출차를 안한 것이다
        # 따라서 마지막 시간을 추가로 넣어준다
        if len(value) % 2 == 1:
            value.append("23:59")

        # 이후 쌍을 맞춰서 시간을 계산한다
        t = 0
        for i in range(len(value) // 2):
            in_time = list(map(int, value[0 + 2 * i].split(':')))
            out_time = list(map(int, value[1 + 2 * i].split(':')))
            # 분이 더 작다면
            if out_time[1] < in_time[1]:
                out_time[0] -= 1
                out_time[1] += 60

            t += 60 * (out_time[0] - in_time[0]) + (out_time[1] - in_time[1])

        # 시간 정보를 저장해준다
        total.append([key, t])

    total.sort(key=lambda x: x[0])

    # 요금 계산
    answer = []
    for t in total:
        if t[1] <= fees[0]:
            answer.append(fees[1])
            continue
        else:
            temp = fees[1]
            t[1] -= fees[0]
            if t[1] % fees[2] == 0:
                temp += t[1] // fees[2] * fees[3]
            else:
                temp += (t[1] // fees[2] + 1) * fees[3]

            answer.append(temp)

    return answer