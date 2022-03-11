# -*- coding: utf-8 -*-
from collections import deque


def solution(cacheSize, cities):
    # 0인 경우는 예외처리를 해준다
    if cacheSize == 0:
        return len(cities) * 5

    time = 0
    cache = deque()
    # time 계산은 크게 두 가지로. 하나는 queue에 있을 경우, 다른 하나는 queue에 없을 경우이다.
    # 만약 캐시에 있다면 1을 더하고 queue의 뒤로 보낸다.
    # 없을 경우는 다시 구 가지로 하나는 queue에 공간이 있을 경우, 다른 하나는 공간이 없을 경우이다.
    for city in cities:
        city = city.lower()
        # 없을 경우
        if city not in cache:
            time += 5
            # 공간이 있을 경우
            if len(cache) < cacheSize:
                cache.append(city)
            # 공간이 없는 경우
            else:
                cache.popleft()
                cache.append(city)

        # 있을 경우
        else:
            time += 1
            cache.remove(city)
            cache.append(city)

    return time
