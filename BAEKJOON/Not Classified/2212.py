import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensors = list(map(int, sys.stdin.readline().split()))

if k >= n:
    print(0)
    sys.exit()

sensors.sort()

dist = []
for i in range(1, len(sensors)):
    dist.append(sensors[i] - sensors[i - 1])

for _ in range(k - 1):
    del_dist = max(dist)
    dist.remove(del_dist)

print(sum(dist))
