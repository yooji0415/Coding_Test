import copy


# 12시 방향부터 시계방향 순서로 들어간다.
# [12, 1.5, 3, 4.5, 6, 7.5, 9, 10.5]
def spin(wheels, wheel_num, t):
    wheel = wheels[wheel_num]
    # 1이면 시계방향 회전이다.
    if t == 1:
        wheel = [wheel[7]] + wheel[:7]
    else:
        wheel = wheel[1:] + [wheel[0]]
    wheels[wheel_num] = wheel


def simulate(original_wheels, wheel_num, t):
    # 어차피 돌릴 수 있는 초이스는 4개니 이걸 그냥 나누자
    wheels = copy.deepcopy(original_wheels)
    if wheel_num == 0:
        spin(wheels, wheel_num, t)
        now = 0
        while now < 3:
            if original_wheels[now][2] == original_wheels[now + 1][6]:
                break
            t *= -1
            now += 1
            spin(wheels, now, t)
    elif wheel_num == 3:
        spin(wheels, wheel_num, t)
        now = 3
        while now > 0:
            if original_wheels[now - 1][2] == original_wheels[now][6]:
                break
            t *= -1
            now -= 1
            spin(wheels, now, t)
    elif wheel_num == 1:
        spin(wheels, wheel_num, t)
        if original_wheels[wheel_num][6] != original_wheels[wheel_num - 1][2]:
            spin(wheels, wheel_num - 1, t * -1)
        now = 1
        while now < 3:
            if original_wheels[now][2] == original_wheels[now + 1][6]:
                break
            t *= -1
            now += 1
            spin(wheels, now, t)
    else:
        spin(wheels, wheel_num, t)
        if original_wheels[wheel_num][2] != original_wheels[wheel_num + 1][6]:
            spin(wheels, wheel_num + 1, t * -1)
        now = 2
        while now > 0:
            if original_wheels[now - 1][2] == original_wheels[now][6]:
                break
            t *= -1
            now -= 1
            spin(wheels, now, t)
    return wheels


wheels = []
for _ in range(4):
    wheels.append(list(map(int, list(input()))))

k = int(input())
for _ in range(k):
    wheel_num, t = map(int, input().split())
    wheel_num -= 1
    wheels = simulate(wheels, wheel_num, t)

answer = 0
for i in range(4):
    wheel = wheels[i]
    if wheel[0] == 1:
        answer += 2**i

print(answer)
