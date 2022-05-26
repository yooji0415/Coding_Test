import sys


N, S = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
answer = 1000000
sp, np = 0, 0
temp = num_list[0]

while True:
    # 만약 총 합이 S 보다 크면 시작 점을 이동
    if temp >= S:
        # 더 작은 경우에는 저장
        if answer > np - sp + 1:
            answer = np - sp + 1

        temp -= num_list[sp]
        sp += 1

    # 만약 총 합이 S 보다 작으면 끝점을 이동
    else:
        if np < N - 1:
            np += 1
            temp += num_list[np]
        else:
            break

if answer == 1000000:
    print(0)
else:
    print(answer)
