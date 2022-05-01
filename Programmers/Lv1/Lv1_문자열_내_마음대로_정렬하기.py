def solution(strings, n):
    sort_index = []
    strings.sort()
    for i, s in enumerate(strings):
        sort_index.append([s[n], i])

    sort_index.sort(key=lambda x: x[0])
    answer = []
    for item in sort_index:
        answer.append(strings[item[1]])

    return answer