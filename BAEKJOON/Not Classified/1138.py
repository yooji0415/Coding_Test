import sys

N = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))
answer_list = [0] * N
for i, num in enumerate(num_list):
    # print(f"num = {num}")
    pos = 0
    for j in range(len(num_list)):
        if num == 0:
            if answer_list[j] != 0:
                continue
            pos = j
            break
        if answer_list[j] == 0:
            num -= 1
        # print(f"cnt = {num}")

    answer_list[pos] = i + 1
    # print(f"answer_list = {answer_list}")

for ans in answer_list:
    print(ans, end=" ")
