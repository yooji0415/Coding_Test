from collections import deque
# 컨베이어 벨트 길이 n, 내구도가 0인 칸이 K개 이상이면 종료
n, k = map(int, input().split())
array = list(map(int, input().split()))
robots = deque([])


def spin(array, robots):
    new_array = [array[-1]] + array[0:-1]
    new_robots = deque([])
    for i in range(len(robots)):
        robot = robots[i]
        if robot + 1 == n - 1:
            continue
        new_robots.append(robots[i] + 1)
    return new_array, new_robots


def robot_move(array, robots):
    new_robots = deque([])
    for i in range(len(robots) - 1, -1, -1):
        pos = robots[i]
        n_pos = pos + 1
        # 이동 할 수 없는 경우
        if n_pos in new_robots or array[n_pos] <= 0:
            new_robots.appendleft(pos)
            continue
        # 이동 가능한 경우
        # 마지막 칸인 경우
        if n_pos == n - 1:
            array[n_pos] -= 1
            continue

        array[n_pos] -= 1
        new_robots.appendleft(n_pos)
    return array, new_robots


def put_robot(array, robots):
    if array[0] != 0:
        robots.appendleft(0)
        array[0] -= 1
    return array, robots


def stop_simulate():
    result = array.count(0)
    return False if result < k else True


flag = False
answer = 0
while not flag:
    answer += 1
    array, robots = spin(array, robots)
    array, robots = robot_move(array, robots)
    array, robots = put_robot(array, robots)
    flag = stop_simulate()

print(answer)
