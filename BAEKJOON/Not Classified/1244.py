import sys


# 스위치 개수
n_sw = int(sys.stdin.readline())
# 스위치 상태
switch = list(map(int, sys.stdin.readline().split()))
switch = [0] + switch
# 학생수
n_st = int(sys.stdin.readline())
# 학생 정보
student = []
for _ in range(n_st):
    student.append(list(map(int, sys.stdin.readline().split())))


# 알고리즘
def change_num(num):
    if num == 1:
        return 0
    else:
        return 1


# 남자
def boy(switch_num):
    idx = switch_num
    seq = 1
    while idx * seq < n_sw + 1:
        switch[idx * seq] = change_num(switch[idx * seq])
        seq += 1


# 여자
def girl(switch_num):
    start = switch_num
    end = switch_num
    while start > 0 and end < n_sw + 1:
        if switch[start] == switch[end]:
            if start == end:
                switch[start] = change_num(switch[start])
            else:
                switch[start] = change_num(switch[start])
                switch[end] = change_num(switch[end])
        else:
            break

        start -= 1
        end += 1


for s in student:
    sex, switch_num = s[0], s[1]
    if sex == 1:
        boy(switch_num)
    else:
        girl(switch_num)


for i in range(1, len(switch)):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()
