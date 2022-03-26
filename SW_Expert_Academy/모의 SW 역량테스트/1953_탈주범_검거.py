T = int(input())
# 상하좌우 순으로 연결 가능한 조합을 만들어둔다.
connect = {
    1: [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]],
    2: [[1, 2, 5, 6], [1, 2, 4, 7], [], []],
    3: [[], [], [1, 3, 4, 5], [1, 3, 6, 7]],
    4: [[1, 2, 5, 6], [], [], [1, 3, 6, 7]],
    5: [[], [1, 2, 4, 7], [], [1, 3, 6, 7]],
    6: [[], [1, 2, 4, 7], [1, 3, 4, 5], []],
    7: [[1, 2, 5, 6], [], [1, 3, 4, 5], []]
}
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    # BFS
    v = [[0] * M for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = []
    q.append([R, C])
    v[R][C] = 1
    while q:
        now = q.pop(0)
        x = now[1]
        y = now[0]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 좌표가 범위 안이고, 방문하지 않은 노드이며, 서로 연결이 가능한 파이프이면
            if -1 < ny < N and -1 < nx < M and v[ny][nx] == 0 and matrix[ny][nx] in connect[matrix[y][x]][i]:
                q.append([ny, nx])
                v[ny][nx] = v[y][x] + 1

    answer = 0
    for y in range(N):
        for x in range(M):
            if v[y][x] != 0 and v[y][x] <= L:
                answer += 1

    print("#{} {}".format(tc, answer))