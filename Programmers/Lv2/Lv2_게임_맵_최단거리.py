# -*- coding: utf-8 -*-
from collections import deque


# 길을 찾는 함수
def find_route(mat, n, m):
    # 노드들을 저장할 queue 생성
    q = deque()
    # 방문 유무 및 경로 길이를 저장할 matrix
    visited = [[0] * m for _ in range(n)]
    q.append([0, 0])
    visited[0][0] = 1
    dx_list = [-1, 1, 0, 0]
    dy_list = [0, 0, -1, 1]
    # q를 돌면서 진행한다.
    while q:
        temp = q.popleft()
        x = temp[1]
        y = temp[0]
        for dx, dy in zip(dx_list, dy_list):
            if -1 < dx + x < m and -1 < dy + y < n and visited[dy + y][dx + x] == 0 and mat[dy + y][dx + x] == 1:
                visited[dy + y][dx + x] = visited[y][x] + 1
                q.append([dy + y, dx + x])

    for i in range(n):
        print(visited[i])
    return visited[n-1][m-1]


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = find_route(maps, n, m)
    if answer == 0:
        return -1
    else:
        return answer

