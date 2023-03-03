import copy
from collections import deque


def check_can_open(graph, lock_len):
    for y in range(lock_len):
        for x in range(lock_len):
            num = graph[y + lock_len][x + lock_len]
            if num == 0 or num == 2:
                return False

    return True


def solution(key, lock):
    lock_len = len(lock)
    key_len = len(key)
    # 키 어레이를 만든다.
    keys = []
    temp = copy.deepcopy(key)
    for i in range(4):
        if i == 0:
            keys.append(temp)
            continue

        result = []
        for x in range(key_len):
            new_line = deque([])
            for y in range(key_len):
                new_line.appendleft(key[y][x])
            result.append(list(new_line))
        key = result
        keys.append(key)

    # 일단 자물쇠의 3배 규격으로 정한다.
    graph = [[0] * (lock_len * 3) for _ in range(lock_len * 3)]
    # 그리고 내부에 이제 값을 넣는다.
    for y in range(lock_len):
        for x in range(lock_len):
            graph[y + lock_len][x + lock_len] = lock[y][x]
    # 그래프 확인용
    # for line in graph:
    #     print(line)

    # 이제 순차적으로 검증을 하면 될 것 같다.
    for candi_key in keys:
        for y_point in range(lock_len * 2):
            for x_point in range(lock_len * 2):
                temp_graph = copy.deepcopy(graph)

                for y in range(key_len):
                    for x in range(key_len):
                        temp_graph[y + y_point][x + x_point] += candi_key[y][x]

                if check_can_open(temp_graph, lock_len):
                    return True

    return False
