import sys


n_list = sys.stdin.readline().strip()

num_dict = {x: 0 for x in range(10)}
for i in range(len(n_list)):
    num_dict[int(n_list[i])] += 1

sorted_num_dict = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)

if sorted_num_dict[0][0] in [6, 9]:
    cnt_six = num_dict[6]
    cnt_nine = num_dict[9]
    temp = cnt_nine + cnt_six
    if temp % 2 == 1:
        temp = temp // 2 + 1
    else:
        temp //= 2

    if temp > sorted_num_dict[1][1]:
        print(temp)
    else:
        print(sorted_num_dict[1][1])

else:
    print(sorted_num_dict[0][1])
