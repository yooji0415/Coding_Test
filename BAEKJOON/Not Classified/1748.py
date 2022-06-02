import sys


n = sys.stdin.readline().strip()
int_n = int(n)
len_n = len(n)
ran = 10
answer = 0
for i in range(len_n):
    if i == len_n - 1:
        answer += (i + 1) * (int_n - ran ** i + 1)
    else:
        answer += (i + 1) * (ran ** (i + 1) - ran ** i)

print(answer)
