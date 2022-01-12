while True:
    num_list = list(map(int, input().split()))
    if sum(num_list) == 0:
        break
    else:
        max_num = max(num_list)
        num_list.remove(max_num)
        if max_num * max_num == num_list[0] * num_list[0] + num_list[1] * num_list[1]:
            print("right")
        else:
            print("wrong")