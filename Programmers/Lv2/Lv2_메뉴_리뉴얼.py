from itertools import combinations


def solution(orders, course):
    answer = []
    result_dict = {}
    for c in course:
        result_dict[c] = {}

    for o in orders:
        o_list = list(o)
        o_list.sort()
        for c in course:
            if c > len(o_list):
                break
            combi_list = combinations(o_list, c)
            for combi in combi_list:
                combi_str = "".join(combi)
                if combi_str not in result_dict[c]:
                    result_dict[c][combi_str] = 1
                else:
                    result_dict[c][combi_str] += 1

    # print(result_dict)
    for course_len, course_cnt in result_dict.items():
        max_cnt = 1
        max_list = []
        for key, value in course_cnt.items():
            if value > max_cnt:
                max_cnt = value
                max_list = [key]
            elif max_cnt != 1 and value == max_cnt:
                max_list.append(key)

        if max_list:
            answer.extend(max_list)

    answer.sort()
    return answer


# print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
