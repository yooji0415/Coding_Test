from itertools import combinations


def solution(infos, querys):
    answer = []
    # 발생할 수 있는 모든 조합에 대해서 dict 처리
    info_dict = {}
    for info in infos:
        temp = info.split(' ')
        key = temp[0:-1]
        value = int(temp[-1])

        for i in range(5):
            combi = list(combinations(key, i))
            for c in combi:
                temp_key = ''.join(c)
                if temp_key not in info_dict:
                    info_dict[temp_key] = []
                info_dict[temp_key].append(value)

    # 이진탐색을 위해서 정렬
    for key in info_dict.keys():
        info_dict[key].sort()

    # query 별 값 도출
    for query in querys:
        query = query.replace('and', '')
        query = query.replace('-', '')
        query = query.split()
        q_key = ''.join(query[:-1])
        q_value = int(query[-1])

        if q_key not in info_dict:
            answer.append(0)
            continue

        s_list = info_dict[q_key]
        left, right = 0, len(s_list)
        while left < right:
            mid = (left + right) // 2
            if s_list[mid] >= q_value:
                right = mid
            else:
                left = mid + 1

        answer.append(len(s_list) - left)

    return answer

