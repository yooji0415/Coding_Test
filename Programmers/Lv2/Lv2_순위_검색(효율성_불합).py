def solution(info, query):
    member = [i for i in range(len(info))]
    lang = {
        'cpp': [],
        'java': [],
        'python': []
    }
    pos = {
        "backend": [],
        "frontend": []
    }
    career = {
        'junior': [],
        'senior': []
    }
    food = {
        'chicken': [],
        'pizza': []
    }
    score = [0 for _ in range(len(info))]

    for n, i in enumerate(info):
        i_list = i.split()
        lang[i_list[0]].append(n)
        pos[i_list[1]].append(n)
        career[i_list[2]].append(n)
        food[i_list[3]].append(n)
        score[n] = int(i_list[4])

    answer = []
    # list(set(lst1) & set(lst2))
    for q in query:
        temp = member
        q = q.replace('and', '')
        q_list = q.split()
        for i in q_list[:-1]:
            if i == '-':
                continue
            if i in ['cpp', 'java', 'python']:
                temp = list(set(temp) & set(lang[i]))
            elif i in ['backend', 'frontend']:
                temp = list(set(temp) & set(pos[i]))
            elif i in ['junior', 'senior']:
                temp = list(set(temp) & set(career[i]))
            elif i in ['chicken', 'pizza']:
                temp = list(set(temp) & set(food[i]))

        result = 0
        for i in temp:
            if score[i] >= int(q_list[-1]):
                result += 1

        answer.append(result)

    return answer

