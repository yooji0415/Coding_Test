import sys

t = int(sys.stdin.readline())
cnt_dict = {
    1: 1,
    2: 2,
    3: 4
}
for n in range(4, 12):
    cnt_dict[n] = cnt_dict[n-1] + cnt_dict[n-2] + cnt_dict[n-3]

for _ in range(t):
    n = int(sys.stdin.readline())
    print(cnt_dict[n])
