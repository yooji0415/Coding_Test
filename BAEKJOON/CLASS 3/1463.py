import sys

n = int(sys.stdin.readline().strip())
cnt_dict = {
    0: 0,
    1: 0,
    2: 1,
    3: 1
}
number = 1
while number < n:
    if 2 * number not in cnt_dict:
        cnt_dict[2 * number] = cnt_dict[number] + 1
    else:
        cnt_dict[2 * number] = min(cnt_dict[2 * number], cnt_dict[number] + 1)

    if 3 * number not in cnt_dict:
        cnt_dict[3 * number] = cnt_dict[number] + 1
    else:
        cnt_dict[2 * number] = min(cnt_dict[3 * number], cnt_dict[number] + 1)

    if 1 + number not in cnt_dict:
        cnt_dict[1 + number] = cnt_dict[number] + 1
    else:
        cnt_dict[1 + number] = min(cnt_dict[1 + number], cnt_dict[number] + 1)

    number += 1

print(cnt_dict[n])
