from bisect import bisect_left, bisect_right


def find_cnt(query, array):
    left_query = query.replace("?", "a")
    right_query = query.replace("?", "z")
    left = bisect_left(array, left_query)
    right = bisect_right(array, right_query)
    return right - left


def solution(words, queries):
    original = {}
    reverse = {}
    for word in words:
        length = len(word)
        if length not in original:
            original[length] = [word]
            reverse[length] = [word[::-1]]
        else:
            original[length].append(word)
            reverse[length].append(word[::-1])

    for key in original.keys():
        original[key].sort()
        reverse[key].sort()

    answer = []
    for query in queries:
        length = len(query)
        if length not in original:
            answer.append(0)
            continue
        if query[0] == "?":
            answer.append(find_cnt(query[::-1], reverse[length]))
        else:
            answer.append(find_cnt(query, original[length]))

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
