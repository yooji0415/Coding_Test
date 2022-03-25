# -*- coding: utf-8 -*-
from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    s = 0
    truck = deque(truck_weights)
    b = deque()
    while truck:
        time += 1
        if b and time - b[0][1] == bridge_length:
            s -= b[0][0]
            b.popleft()

        if len(b) < bridge_length and s + truck[0] <= weight:
            s += truck[0]
            b.append([truck.popleft(), time])

        # print("시간 : {} 다리 : {}".format(time, b))

    while b:
        time += 1
        if time - b[0][1] == bridge_length:
            b.popleft()
        # print("시간 : {} 다리 : {}".format(time, b))

    return time


