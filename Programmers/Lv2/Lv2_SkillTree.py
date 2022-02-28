def solution(skill, skill_trees):
    s = list(skill)
    cnt = 0
    for st in skill_trees:
        idx = [100000] * len(s)
        is_right = True
        for i in range(len(s)):
            if s[i] in st:
                temp = st.index(s[i])
                idx[i] = temp

        for i in range(1, len(s)):
            if idx[i] < idx[i - 1]:
                is_right = False
                break

        if is_right:
            cnt += 1

    return cnt


# 모범답안
# 동일 기능을 stack을 통해서 진행했다
def best_solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

