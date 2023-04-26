def solution(table, languages, preference):
    datas = []
    titles = []
    for line in table:
        array = line.split(" ")
        datas.append(array[1:])
        titles.append(array[0])

    scores = [0] * len(titles)
    for i in range(len(languages)):
        lang = languages[i]
        prefer = preference[i]
        for j in range(len(datas)):
            data = datas[j]
            result = 0
            for k in range(len(data)):
                if data[k] == lang:
                    result = len(data) - k
                    break
            scores[j] += result * prefer

    max_idx = [0]
    max_val = -1
    for i in range(len(scores)):
        if scores[i] >= max_val:
            if max_val == scores[i]:
                max_idx.append(i)
            else:
                max_val = scores[i]
                max_idx = [i]
    answer = [titles[i] for i in max_idx]
    answer.sort()
    return answer[0]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))
