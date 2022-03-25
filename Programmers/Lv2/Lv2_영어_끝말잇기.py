def solution(n, words):
    now = ""
    prev = ""
    word_list = []
    for i in range(len(words)):
        if i == 0:
            prev = words[i]
            word_list.append(prev)
            continue

        now = words[i]
        if prev[-1] != now[0] or now in word_list:
            return [i % n + 1, i // n + 1]
        else:
            prev = now
            word_list.append(now)

    return [0, 0]
