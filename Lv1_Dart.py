import math


def solution(dartResult):
    score_list = []
    option_list = []
    bonus_dict = {
        "S": 1,
        "D": 2,
        "T": 3
    }
    for i in range(1, len(dartResult)):
        # 알파벳 기준 슬라이싱을 생각함
        if dartResult[i].isalpha():
            # 다음이 옵션인지 아닌지 확인
            if i + 1 < len(dartResult):
                if dartResult[i+1] in ["*", "#"]:
                    option_list.append(dartResult[i+1])
                else:
                    option_list.append("n")
            else:
                option_list.append("n")

            # 옵션을 뺀 점수를 넣는다.
            score = 0
            if i >= 2:
                if dartResult[i-1] == "0" and dartResult[i-2] == "1":
                    score = 10
                else:
                    score = int(dartResult[i - 1])
            else:
                score = int(dartResult[i-1])

            score = pow(score, int(bonus_dict[dartResult[i]]))
            score_list.append(score)

    print(option_list)
    print(score_list)
    for j in range(len(option_list)):
        if j == 0:
            if option_list[j] == "*":
                score_list[j] *= 2
            elif option_list[j] == "#":
                score_list[j] *= -1
        else:
            if option_list[j] == "*":
                score_list[j] *= 2
                score_list[j-1] *= 2
            elif option_list[j] == "#":
                score_list[j] *= -1

    print(score_list)
    return sum(score_list)


# 모범답안
# 숫자 10으로 인한 예외상황이 많았는데 이를 다른 문자로
# 전환해서 하는 방법과 이를 리스트로 전환해서 처리하는 방법을 배웠다.
def best_solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)


print(best_solution("1S2D*3T"))