import sys

# 재귀 제한 상향
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))

# 인덱스 값을 찾기 쉽게 하기 위한 장치
index_list = [0] * (n + 1)
for i in range(n):
    index_list[in_order[i]] = i


def pre_order(in_s, in_e, pos_s, pos_e):
    if in_s > in_e or pos_s > pos_e:
        return

    # 루트 값을 찾는다
    root = post_order[pos_e]
    root_index = index_list[root]
    left = root_index - in_s
    right = in_e - root_index

    # 출력 이후 제귀 진행
    print(root, end=" ")
    pre_order(in_s, in_s + left - 1, pos_s, pos_s + left - 1)
    pre_order(in_e - right + 1, in_e, pos_e - right, pos_e - 1)


pre_order(0, n - 1, 0, n - 1)
