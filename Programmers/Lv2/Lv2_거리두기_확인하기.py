from collections import deque as dq


def bfs(plist, table):
    # 사람 위치마다 bfs
    for p in plist:
        # 방문처리
        visited = [[0 for _ in range(5)] for _ in range(5)]
        # 거리처리
        d = [[0 for _ in range(5)] for _ in range(5)]
        # 넣을 준비
        q = dq()
        q.append([p[0], p[1]])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        # 반복처리
        while q:
            nlocs = []
            loc = q.popleft()
            x = loc[1]
            y = loc[0]
            visited[y][x] = 1

            for i in range(4):
                nlocs.append([y + dy[i], x + dx[i]])

            for nloc in nlocs:
                nx = nloc[1]
                ny = nloc[0]
                if -1 < ny < 5 and -1 < nx < 5:
                    d[ny][nx] = d[y][x] + 1
                    if d[ny][nx] >= 3 or visited[ny][nx] == 1:
                        continue
                    if table[ny][nx] == 'P':
                        return 0
                    elif table[ny][nx] == 'O':
                        q.append(nloc)
                    else:
                        continue

    return 1


def solution(places):
    answer = []
    # 입력 마다
    for place in places:
        table = []
        plist = []

        # 한 입력에 대해서
        for l in place:
            table.append(list(l))

        # 테이블
        for y in range(5):
            for x in range(5):
                if table[y][x] == 'P':
                    plist.append([y, x])

        # 결과
        result = bfs(plist, table)
        answer.append(result)

    return answer

