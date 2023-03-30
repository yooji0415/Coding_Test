n, m = map(int, input().split())
balls = list(map(int, input().split()))

cnt = 0

for i in range(n):
    now = balls[i]
    for j in range(i + 1, n):
        if balls[j] != now:
            cnt += 1

print(cnt)
