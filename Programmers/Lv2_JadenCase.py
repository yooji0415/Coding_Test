# 상당히 짧은 코드지만 알아간 것이 많다.
# 우선 for 문을 리스트에서 받아오는 형식으로 만들면
# 값을 변경해도 반영이 안된다.
# 두 번째로는 split() 함수에 값을 안주는 디폴트를 쓰면
# 공백이 몇 칸 연속으로 오더라도 무시하고 잘라준다.
# 세 번째는 capitalize() 함수는 해당 문자열의 맨 앞을 대문자로 만든다.
def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    answer =' '.join(s)
    return answer
