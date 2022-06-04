import sys


def check_points(grp, step, s_x, s_y):
    temp_list = [grp[s_y][s_x], grp[s_y + step][s_x], grp[s_y][s_x + step], grp[s_y + step][s_x + step]]
    first_num = temp_list[0]
    for num in temp_list[1:]:
        if num != first_num:
            return False

    return True


n, m = map(int, sys.stdin.readline().split())
grp = []
for _ in range(n):
    grp.append(list(map(int, list(sys.stdin.readline().strip()))))

# print(grp)
max_len = min(n - 1, m - 1)
answer = 1
for step in range(0, max_len + 1):
    for y in range(0, n - step):
        for x in range(0, m - step):
            # print(f"x : {x} y : {y} step: {step}")
            if check_points(grp, step, x, y):
                answer = (step + 1) ** 2

print(answer)
