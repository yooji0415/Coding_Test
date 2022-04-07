def solution(dirs):
    answer = 0
    # 길을 다 str으로 x1y1x2y2 모양으로 처리하면 어떤가?
    now_pos = [0, 0]
    dir_dict = {
        'U': [0, 1],
        'D': [0, -1],
        'R': [1, 0],
        'L': [-1, 0]
    }
    load_list = []
    for d in dirs:
        dxdy = dir_dict[d]
        next_pos = [now_pos[0] + dxdy[0], now_pos[1] + dxdy[1]]
        if -6 < next_pos[0] < 6 and -6 < next_pos[1] < 6:
            temp = ''.join(map(str, now_pos)) + ''.join(map(str, next_pos))
            load_list.append(temp)
            now_pos = next_pos

    load_list = set(load_list)
    return len(load_list)

