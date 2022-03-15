# -*- coding: utf-8 -*-
from collections import deque


def solution(record):
    answer = []
    enter = "님이 들어왔습니다."
    leave = "님이 나갔습니다."
    user_d = {}
    in_out_q = deque()
    for r in record:
        temp = r.split()
        if temp[0] == "Enter":
            if temp[1] not in user_d or temp[2] != user_d[temp[1]]:
                user_d[temp[1]] = temp[2]
            in_out_q.append([1, temp[1]])
        elif temp[0] == "Leave":
            in_out_q.append([0, temp[1]])
        else:
            user_d[temp[1]] = temp[2]

    while in_out_q:
        temp = in_out_q.popleft()
        if temp[0] == 1:
            answer.append(user_d[temp[1]] + enter)
        else:
            answer.append(user_d[temp[1]] + leave)

    return answer
