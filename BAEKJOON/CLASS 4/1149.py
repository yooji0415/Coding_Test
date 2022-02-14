import sys

n = int(sys.stdin.readline())
value_list = []
for _ in range(n):
    value_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, len(value_list)):
    value_list[i][0] = min(value_list[i - 1][1], value_list[i - 1][2]) + value_list[i][0]
    value_list[i][1] = min(value_list[i - 1][0], value_list[i - 1][2]) + value_list[i][1]
    value_list[i][2] = min(value_list[i - 1][0], value_list[i - 1][1]) + value_list[i][2]

print(min(value_list[n - 1][0], value_list[n - 1][1], value_list[n - 1][2]))
