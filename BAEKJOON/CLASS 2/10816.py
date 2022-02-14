n = int(input())
n_list = list(map(int, input().split(" ")))
n_list.sort()
n_dict = dict()
m = int(input())
m_list = list(map(int, input().split(" ")))

for num in n_list:
    if num in n_dict:
        n_dict[num] += 1
    else:
        n_dict[num] = 1

cnt = ""
for num in m_list:
    if num in n_dict:
        print(n_dict[num], end= " ")
    else:
        print(0, end=" ")

# 정렬을 하고 안하고의 시간 차이가 존재한다.
# 처음에는 정렬하는 시간이 더 오래 소모되어
# 실용적이자 않다고 생각했는데
# 실질적으로는 정렬하고 반복문을 진행하는게 더 효율적이였다.
