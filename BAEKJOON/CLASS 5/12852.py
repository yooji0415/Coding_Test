import sys


number = int(sys.stdin.readline().strip())
num_list = [[0, []] for _ in range(number + 1)]
num_list[1][0] = 0
num_list[1][1] = [1]

for i in range(2, number + 1):
    num_list[i][0] = num_list[i - 1][0] + 1
    num_list[i][1] = num_list[i - 1][1] + [i]

    if i % 3 == 0 and num_list[i][0] > num_list[i // 3][0] + 1:
        num_list[i][0] = num_list[i // 3][0] + 1
        num_list[i][1] = num_list[i // 3][1] + [i]

    if i % 2 == 0 and num_list[i][0] > num_list[i // 2][0] + 1:
        num_list[i][0] = num_list[i // 2][0] + 1
        num_list[i][1] = num_list[i // 2][1] + [i]

print(num_list[number][0])
for i in range(len(num_list[number][1]) - 1, -1, -1):
    print(num_list[number][1][i], end=" ")
