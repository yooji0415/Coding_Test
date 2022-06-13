import sys


w_list = []
p_list = []

while True:
    word = sys.stdin.readline().strip()
    if word == "-":
        break
    w_list.append(word)

while True:
    puzzle = sys.stdin.readline().strip()
    p_dict = {}
    if puzzle == "#":
        break
    p_temp_list = sorted(list(puzzle))
    for p in p_temp_list:
        if p not in p_dict:
            p_dict[p] = {"cnt": 1, "used": 0}
        else:
            p_dict[p]["cnt"] += 1

    p_list.append(p_dict)

for p_dict in p_list:
    for word in w_list:
        flag = True
        w_set = set(word)
        for w in w_set:
            if w not in p_dict or p_dict[w]["cnt"] < word.count(w):
                flag = False
                break
        if flag:
            for w in w_set:
                p_dict[w]["used"] += 1

    min_cnt, max_cnt = 200001, 0
    min_words, max_words = [], []
    for key in p_dict:
        if p_dict[key]["used"] >= max_cnt:
            if max_cnt == p_dict[key]["used"]:
                max_words.append(key)
            else:
                max_cnt = p_dict[key]["used"]
                max_words = [key]

        if p_dict[key]["used"] <= min_cnt:
            if min_cnt == p_dict[key]["used"]:
                min_words.append(key)
            else:
                min_cnt = p_dict[key]["used"]
                min_words = [key]

    print("".join(min_words), min_cnt, "".join(max_words), max_cnt)
