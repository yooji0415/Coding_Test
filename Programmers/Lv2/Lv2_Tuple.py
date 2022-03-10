def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key= len)
    for t in s:
        temp = t.split(',')
        for num in temp:
            if int(num) not in answer:
                answer.append(int(num))
    return answer
