# -*- coding: utf-8 -*-
import heapq  # 우선순위 큐 구현을 위함


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return distances


def solution(N, road, K):
    graph = {x: {} for x in range(1, N + 1)}
    for r in road:
        if r[1] not in graph[r[0]]:
            graph[r[0]][r[1]] = r[2]
        else:
            graph[r[0]][r[1]] = min(r[2], graph[r[0]][r[1]])
        if r[0] not in graph[r[1]]:
            graph[r[1]][r[0]] = r[2]
        else:
            graph[r[1]][r[0]] = min(r[2], graph[r[1]][r[0]])

    distances = dijkstra(graph, 1)
    answer = 0
    for key, value in distances.items():
        if value <= K:
            answer += 1

    return answer

