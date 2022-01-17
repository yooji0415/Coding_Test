import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))
temp_set = set(input_list)
sorted_list = sorted(list(temp_set))
answer_dict = {}
for i in range(len(sorted_list)):
    if sorted_list[i] not in answer_dict:
        answer_dict[sorted_list[i]] = i

for item in input_list:
    print(answer_dict[item], end=" ")
