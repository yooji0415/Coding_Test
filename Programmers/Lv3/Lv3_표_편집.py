def solution(n, k, cmd):
    answer = ''
    cell_dict = {}
    del_list = []
    pos = k

    for i in range(n):
        cell_dict[i] = [i - 1, i + 1]

    cell_value = ["O"] * n

    cmd_list = []
    for item in cmd:
        c = item.split()
        if len(c) == 2:
            c[1] = int(c[1])

        if c[0] == "U":
            for _ in range(c[1]):
                pos = cell_dict[pos][0]

        elif c[0] == "D":
            for _ in range(c[1]):
                pos = cell_dict[pos][1]

        elif c[0] == "C":
            cell_value[pos] = "X"
            prev, next_ = cell_dict[pos]
            del_list.append([prev, next_, pos])
            if prev == -1:
                cell_dict[next_][0] = -1
                pos = next_
            elif next_ == n:
                cell_dict[prev][1] = n
                pos = prev
            else:
                cell_dict[prev][1] = next_
                cell_dict[next_][0] = prev
                pos = next_

        else:
            prev, next_, value = del_list.pop()
            cell_value[value] = "O"
            if prev == -1:
                cell_dict[next_][0] = value
            elif next_ == n:
                cell_dict[prev][1] = value
            else:
                cell_dict[prev][1] = value
                cell_dict[next_][0] = value

    return "".join(cell_value)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
