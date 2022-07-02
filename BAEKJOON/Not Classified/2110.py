import sys


N, C = map(int, sys.stdin.readline().split())
n_list = []
for _ in range(N):
    temp = int(sys.stdin.readline())
    n_list.append(temp)

n_list.sort()
min_gap = 1
max_gap = n_list[-1] - n_list[0]
answer = 1
while min_gap <= max_gap:
    mid_gap = (min_gap + max_gap) // 2
    cnt, before = 1, n_list[0]
    for num in n_list[1:]:
        if num >= before + mid_gap:
            cnt += 1
            before = num

    if cnt >= C:
        answer = mid_gap
        min_gap = mid_gap + 1
    else:
        max_gap = mid_gap - 1

print(answer)