import sys

n = int(sys.stdin.readline())
cnt = {
    1: 1,
    2: 2
}
if n in cnt:
    print(cnt[n])
    exit(0)

for i in range(3, n+1):
    cnt[i] = (cnt[i-1] + cnt[i-2]) % 10007

print(cnt[i])
