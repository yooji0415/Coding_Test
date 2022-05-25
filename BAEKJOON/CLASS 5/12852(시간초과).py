import sys
import copy

sys.setrecursionlimit(10**6)
number = int(sys.stdin.readline().strip())
num_dict = {
    1: [0, [1]]
}


def find_route(num):
    if num in num_dict:
        return num_dict[num]
    else:
        temp_count_list = []
        temp_list = []
        if num % 3 == 0:
            temp1 = find_route(num // 3)
            temp_list.append(temp1)
            temp1_count = temp1[0] + 1
            temp_count_list.append(temp1_count)

        if num % 2 == 0:
            temp2 = find_route(num // 2)
            temp_list.append(temp2)
            temp2_count = temp2[0] + 1
            temp_count_list.append(temp2_count)

        temp3 = find_route(num - 1)
        temp_list.append(temp3)
        temp3_count = temp3[0] + 1
        temp_count_list.append(temp3_count)

        idx = temp_count_list.index(min(temp_count_list))
        answer = copy.deepcopy(temp_list[idx])
        answer[0] += 1
        answer[1].append(num)
        num_dict[num] = answer
        return answer


answer_list = find_route(number)
# print(num_dict)
# print()
print(answer_list[0])
for i in range(len(answer_list[1]) - 1, -1, -1):
    print(answer_list[1][i], end=" ")
