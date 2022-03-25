from collections import deque


def solution(people, limit):
    answer = 0
    s_people = sorted(people, reverse= True)
    s_people = deque(s_people)
    while s_people:
        if len(s_people) == 1:
            answer += 1
            s_people.pop()
        else:
            if s_people[0] + s_people[-1] <= limit:
                s_people.pop()
                s_people.popleft()
                answer += 1
            else:
                s_people.popleft()
                answer += 1

    return answer
