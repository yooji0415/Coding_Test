import sys

N = int(sys.stdin.readline().strip())
num_list = {x: 0 for x in range(1, 10001)}
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    num_list[num] += 1

for i in range(1, 10001):
    for _ in range(num_list[i]):
        print(i)
