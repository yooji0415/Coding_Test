def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break

        if i == len(completion) - 1:
            answer = participant[i + 1]
            break

    return answer


# 모범답안
# 정렬을 한 후 하나씩 비교하는 생각을 했으나 
# hash 함수를 사용해서 숫자를 통한 합산 방법이 참신했다
def best_solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer