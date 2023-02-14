import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

arr_1 = arr[:n // 2]
arr_2 = arr[n // 2:]

subsum_arr1 = []
subsum_arr2 = []

for i in range(len(arr_1) + 1):
    comb_1 = combinations(arr_1, i)
    for comb in comb_1:
        subsum_arr1.append(sum(comb))

for i in range(len(arr_2) + 1):
    comb_2 = combinations(arr_2, i)
    for comb in comb_2:
        subsum_arr2.append(sum(comb))

subsum_arr1.sort()
subsum_arr2.sort()

left = 0
right = len(subsum_arr2) - 1
answer = 0

while left < len(subsum_arr1) and right >= 0:
    temp = subsum_arr1[left] + subsum_arr2[right]

    if temp == s:
        same_cnt_left = 1
        same_cnt_right = 1

        same_left_idx = left
        same_right_idx = right

        left += 1
        right -= 1

        while left < len(subsum_arr1) and subsum_arr1[left] == subsum_arr1[same_left_idx]:
            same_cnt_left += 1
            left += 1

        while right >= 0 and subsum_arr2[right] == subsum_arr2[same_right_idx]:
            same_cnt_right += 1
            right += 1

        answer + same_cnt_left * same_cnt_right

    elif temp < s:
        left += 1

    else:
        right -= 1

if s == 0:
    answer -= 1

print(answer)

