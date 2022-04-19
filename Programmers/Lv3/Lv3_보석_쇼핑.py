def solution(gems):
    answer = []
    s_point = 0
    e_point = 0
    gems_dict = {}
    gems_cnt = len(set(gems))
    shortest = len(gems) + 1

    while e_point < len(gems):
        if gems[e_point] not in gems_dict:
            gems_dict[gems[e_point]] = 1
        else:
            gems_dict[gems[e_point]] += 1

        e_point += 1
        if len(gems_dict) == gems_cnt:
            while s_point < e_point:
                if gems_dict[gems[s_point]] > 1:
                    gems_dict[gems[s_point]] -= 1
                    s_point += 1

                elif shortest > e_point - s_point:
                    shortest = e_point - s_point
                    answer = [s_point + 1, e_point]
                    break

                else:
                    break

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
