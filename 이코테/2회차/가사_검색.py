from bisect import bisect_left, bisect_right


def find_by_query(arr, query):
    first = query.replace("?", "a")
    last = query.replace("?", "z")

    first_idx = bisect_left(arr, first)
    last_idx = bisect_right(arr, last)

    return last_idx - first_idx


def solution(words, queries):
    answer = []

    normal_arr = [[] for _ in range(100001)]
    reversed_arr = [[] for _ in range(100001)]

    for word in words:
        normal_arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])

    for i in range(2, 100001):
        normal_arr[i].sort()
        reversed_arr[i].sort()

    for query in queries:
        if query[0] != "?":
            answer.append(find_by_query(normal_arr[len(query)], query))
        else:
            answer.append(find_by_query(reversed_arr[len(query)], query[::-1]))

    return answer
