import sys

input = sys.stdin.readline

N, M = map(int, input().split())
# d는 0이면 북, 1이면 동, 2이면 남, 3이면 서 이다.
r, c, direction = map(int, input().split())
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 현재 칸이 아직 청소되지 않은 칸이면 현재 칸 청소
# 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 없으면
#   바라보는 방향을 유지한 채로 한칸 후진할 수 있으면 한칸 후진 후 처음으로
#   후진 불가면 종료
# 4칸중 청소되지 않은 빈칸이 있으면
#   반시계 90도 회전
#   바라보는 방향을 기준으로 앞쪽 칸이 청소 안되어있으면 전진
#   처음으로 고

flag = True
answer = 0
while flag:
    # print(r, c)
    # 현 위치가 청소가 안되있는 경우
    if graph[r][c] == 0:
        graph[r][c] = 2
        answer += 1
        continue

    # 주변에 청소할 곳이 있는지 체크
    is_dirty = False
    for dr, dc in d:
        nr, nc = dr + r, dc + c
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if graph[nr][nc] == 0:
            is_dirty = True
            break

    # 없다면
    if not is_dirty:
        dr, dc = d[direction]
        nr, nc = r - dr, c - dc
        if nr < 0 or nr >= N or nc < 0 or nc >= M or graph[nr][nc] == 1:
            flag = False
            continue
        r, c = nr, nc
        continue

    # 있다면
    for _ in range(4):
        direction = 3 if direction == 0 else direction - 1
        dr, dc = d[direction]
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= M or graph[nr][nc] != 0:
            continue

        r, c = nr, nc
        break

print(answer)
