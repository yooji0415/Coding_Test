# -*- coding: utf-8 -*-
def solution(msg):
    answer = []
    d = {}
    i = 1
    while i < 27:
        d[chr(64 + i)] = i
        i += 1
    now = 0
    nex = 1
    while now < len(msg):
        # 사전에 있는 곳 까지를 순회
        while nex <= len(msg) and msg[now:nex] in d:
            nex += 1
            # print("now : {} nex : {}".format(now, nex))

        # 나왔을 때 위치는 now 는 시작점 nex 는 사전에 없는 위치
        # 사전 및 정답 어레이 업데이트
        answer.append(d[msg[now:nex - 1]])
        d[msg[now:nex]] = i
        i += 1

        # now 와 nex 업데이트
        now = nex - 1
        nex = now + 1

    return answer


# 모범 답안
# 동일 알고리즘이나 좀 더 간략하게 풀어냈다
def best_solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer
