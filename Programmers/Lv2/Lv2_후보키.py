from itertools import combinations as combi


def solution(relation):
    col = len(relation[0])
    idx = [i for i in range(col)]
    combinations = []

    # 모든 조합의 경우의 수를 먼저 담는다
    for i in range(1, col + 1):
        combinations.extend(combi(idx, i))

    # 유일성에 대한 검증부터 한다
    answer = []
    for combination in combinations:
        values = []

        # 모든 행에 대해서 조합안에 있는 속성들만 뽑아 리스트를 만든다
        for row in relation:
            temp = []
            for i in range(len(combination)):
                temp.append(row[combination[i]])
            values.append(temp)

        # 원소들이 겹치는지 확인한다
        is_unique = True
        for value in values:
            if values.count(value) != 1:
                is_unique = False
                break

        # 유일하면 최소성을 확인한다
        if is_unique:
            is_mini = True
            for key in answer:
                if set(key).issubset(combination):
                    is_mini = False
            if is_mini:
                answer.append(combination)

    return len(answer)