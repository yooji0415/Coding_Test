# -*- coding: utf-8 -*-
def solution(files):
    # 먼저 파일을 세 부분으로 나눠서 저장한다
    split_files = []
    for f in files:
        # 숫자의 시작 포인트를 찾는다
        n_start_point = 0
        for i in range(len(f)):
            if f[i].isdigit():
                n_start_point = i
                break

        # 숫자의 끝 포인트를 찾는다
        n_end_point = 0
        for i in range(i, len(f)):
            if not f[i].isdigit():
                n_end_point = i
                break

        if n_end_point == 0:
            n_end_point = len(f)
        # 해당 정보들을 이용해 분할한 파일 이름 정보를 담는다
        temp = [f[:n_start_point], f[n_start_point:n_end_point], f[n_end_point:]]
        split_files.append(temp)

    # 기준에 맞게 정렬해준다
    split_files.sort(key=lambda x: (x[0].lower(), int(x[1])))

    # 정답 리스트를 생성하고 이를 반환해준다
    answer = []
    for f in split_files:
        answer.append(''.join(f))
    return answer
