import sys


n = int(sys.stdin.readline().strip())
answer = []
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

best = 10000000000
best_list = []
sp, ep = 0, n - 1

while sp < ep:
    result = num_list[ep] + num_list[sp]
    if abs(result) < best:
        best = abs(result)
        best_list = [num_list[sp], num_list[ep]]
        if result == 0:
            break

    if result > 0:
        ep -= 1
    elif result < 0:
        sp += 1

print(f"{best_list[0]} {best_list[1]}")
