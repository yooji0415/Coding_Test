def find_block(y, x, l, arr, answer):
    num = arr[y][x]
    is_right = True
    for i in range(y, y + l):
        for j in range(x, x + l):
            if num != arr[i][j]:
                is_right = False
                break

        if not is_right:
            break

    if is_right:
        answer[num] += 1
        return
    else:
        l //= 2
        find_block(y, x, l, arr, answer)
        find_block(y + l, x, l, arr, answer)
        find_block(y, x + l, l, arr, answer)
        find_block(y + l, x + l, l, arr, answer)


def solution(arr):
    answer = [0, 0]
    l = len(arr)
    find_block(0, 0, l, arr, answer)
    return answer

