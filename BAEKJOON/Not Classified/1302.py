import sys


N = int(sys.stdin.readline())
sells = dict()
for _ in range(N):
    sell = sys.stdin.readline().strip()
    if sell not in sells:
        sells[sell] = 1
    else:
        sells[sell] += 1

sorted_sells = sorted(sells.items())
sorted_sells = sorted(sorted_sells, key=lambda item: item[1], reverse=True)
print(sorted_sells[0][0])
