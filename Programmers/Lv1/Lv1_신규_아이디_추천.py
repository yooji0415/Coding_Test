import re


# 정규형을 사용한 풀이법으로 re.sub 함수에 대한 공부가 필요하다 생각을 함
def solution(new_id):
    answer = ''
    # 1단계 대문자를 소문자로 변경
    new_id = new_id.lower()
    # 2단계 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
    new_id = re.sub('[^a-z\d\-\_\.]', '', new_id)
    # 3단계 마침표 2번 이상을 하나로
    new_id = re.sub('\.\.+', '..', new_id)
    # 4단계 양 끝의 마침표 제거
    new_id = re.sub('^\.|\.$', '', new_id)
    # 5단계 빈 문자열이면 a
    if new_id == '':
        new_id = 'a'

    # 6단계 길이가 16자 이상이면 15자 남기고 맨 끝 마침표 제거
    new_id = re.sub('\.$', '', new_id[0:15])
    # 7단계 길이가 3이 될 때까지 반복해서 끝에 붙이기
    while len(new_id) < 3:
        new_id += new_id[-1:]

    answer = new_id
    return answer


# 모범답안
def best_solution(new_id):
    answer = ''
    # 1번 lower 함수를 통해 대문자를 소문자로 바꾼다.
    new_id = new_id.lower()
    # 2번 isalpha, isdigit, 리스트 in 비교를 통한 아이디어다.
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3번 while 루프를 돌면서 replace 를 통해 변경을 해준다.
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4번 처음과 끝을 if 문으로 비교를 해주고 없애준다.
    if answer[0] == '.':
            answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5번 안에가 비었는지 확인 후 변경한다.
    if answer == '':
        answer = 'a'
    # 6번 길이가 15를 넘을경우 잘라주고 마지막에 있는 점을 제거한다.
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7번 길이가 짧을 경우에는 마지막 문자를 계속 더해준다.
    while len(answer) < 3:
        answer += answer[-1]

    return answer
