import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
ans_list = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j] and ans_list[i] < ans_list[j]:
            ans_list[i] = ans_list[j]
    ans_list[i] += 1

print(max(ans_list))
