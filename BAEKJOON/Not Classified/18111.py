import sys

N, M, B = map(int, sys.stdin.readline().split())
land = []
for _ in range(N):
    land.append(list(map(int, sys.stdin.readline().split())))

# 시간복잡도를 생각해보자
# 모든 땅을 다 방문해서 해당 기준으로 맞추는 작업을 생각한다면
# N^2 이 걸릴 것이다. 행, 열이 500으로 상한선이 있으니 나름 할만하다 판단하고 진행하자


def check_result (land_height):
    result = 0
    temp_B = B
    # 땅 영역을 순회한다
    for y in range(N):
        for x in range(M):
            temp = land[y][x]
            if temp < land_height:
                req = land_height - temp
                temp_B -= req
                result += req
            else:
                req = temp - land_height
                temp_B += req
                result += 2 * req

    # 소지 혹은 습득한 땅의 양보다 많은 땅을 사용해야 한다면 이거는 불가능한 경우이다
    if temp_B >= 0:
        return result
    else:
        return -1


answer = [0, 100000000]
for check_num in range(257):
    result = check_result(check_num)
    if result != -1:
        if answer[1] >= result:
            answer = [check_num, result]

print(f"{answer[1]} {answer[0]}")
