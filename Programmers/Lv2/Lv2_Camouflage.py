def solution(clothes):
    dic = {}
    for c in clothes:
        if c[1] not in dic:
            dic[c[1]] = 1

        dic[c[1]] += 1

    answer = 1
    for v in dic.values():
        answer *= v

    return answer - 1
