def solution(numbers, hand):
    answer = ''
    # 키패드를 숫자를 키로 위치좌표를 값으로 설정해 dict 구조로 만든다.
    kp = {
        1: [0, 0],  2: [0, 1], 3: [0, 2],
        4: [1, 0],  5: [1, 1], 6: [1, 2],
        7: [2, 0],  8: [2, 1], 9: [2, 2],
        10: [3, 0], 0: [3, 1], 12: [3, 2]
    }
    # 초기 위치정보를 준다. 쉬운 구조로 만들기 위해서 특수문자를 수로 바꿨다.
    r_loc = 12
    l_loc = 10
    for num in numbers:
        # 우선적으로 좌, 우 줄에 있는 숫자들인지 확인한다.
        if num in [1, 4, 7]:
            answer += 'L'
            l_loc = num
        elif num in [3, 6, 9]:
            answer += 'R'
            r_loc = num
        # 중립지역일 경우 거리를 좌표값으로 절대값 계산을 해준다.
        else:
            l_dis = abs(kp[num][0] - kp[l_loc][0]) + abs(kp[num][1] - kp[l_loc][1])
            r_dis = abs(kp[num][0] - kp[r_loc][0]) + abs(kp[num][1] - kp[r_loc][1])
            # 이후 어느 거리가 짧은지 고려해 값을 입력해준다.
            if l_dis < r_dis:
                answer += 'L'
                l_loc = num
            elif l_dis > r_dis:
                answer += 'R'
                r_loc = num
            # 만약 값이 같으면 주 손으로 비교를 해준다.
            else:
                if hand == "right":
                    answer += 'R'
                    r_loc = num
                else:
                    answer += 'L'
                    l_loc = num

    return answer


# 모범답안
# 제출한 답안과 유사하기 때문에 추가적인 설명은 하지 않았다.
def best_solution(numbers, hand):
    answer = ''
    location = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    left, right = [3, 0], [3, 2]
    for i in numbers:
        if i % 3 == 1:
            answer += 'L'
            left = location[i]
        elif i % 3 == 0 and i != 0:
            answer += 'R'
            right = location[i]
        else:
            l = abs(location[i][0] - left[0]) + abs(location[i][1] - left[1])
            r = abs(location[i][0] - right[0]) + abs(location[i][1] - right[1])
            if l < r:
                answer += 'L'
                left = location[i]
            elif l > r:
                answer += 'R'
                right = location[i]
            else:
                answer += hand[0].upper()
                if hand == 'right':
                    right = location[i]
                else:
                    left = location[i]

    return answer
