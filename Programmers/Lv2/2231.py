import sys


n = int(sys.stdin.readline().strip())
answer = 0

for i in range(1, n):
    i_list = list(map(int, list(str(i))))
    list_sum = sum(i_list)
    if i + list_sum == n:
        answer = i
        break

print(answer)
