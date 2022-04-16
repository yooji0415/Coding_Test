def solution(n, k, cmd):
    answer = ''
    cell = {}
    # 우선 셀을 만든다
    for i in range(n):
        cell[i] = "O"

    cell_list = [i for i in range(n)]
    del_list = []

    # 현 위치를 표시하는 포인터를 만든다
    pos = k

    # 명령을 모두 리스트화 시킨다
    cmd_list = []
    for c in cmd:
        temp = c.split()
        if len(temp) == 2:
            temp[1] = int(temp[1])

        cmd_list.append(temp)

    # 명령을 순차적으로 실행한다.
    for c in cmd_list:
        if c[0] == "U":
            pos -= c[1]
        elif c[0] == "D":
            pos += c[1]
        elif c[0] == "C":
            temp = cell_list.pop(pos)
            cell[temp] = "X"
            del_list.append([temp, pos])
            if len(cell_list) <= pos:
                pos -= 1

        else:
            temp = del_list.pop()
            value, in_pos = temp[0], temp[1]
            cell[value] = "O"
            if pos >= in_pos:
                pos += 1
            cell_list.insert(in_pos, value)

        # print(f"c : {c} / pos : {pos}")
        # print(f"cell list : {cell_list}")
        # print(f"cell : {cell}")
    # 정답을 찾고 보내준다
    answer = ""
    for i in range(n):
        answer = answer + cell[i]

    return answer


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
