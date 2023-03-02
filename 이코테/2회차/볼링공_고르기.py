n, m = map(int, input().split())
balls = list(map(int, input().split()))

ball_dict = {i: 0 for i in range(1, m + 1)}

for ball in balls:
    ball_dict[ball] += 1

answer = 0

print(ball_dict)

for ball in balls:
    answer += n - ball_dict[ball]
    ball_dict[ball] -= 1
    n -= 1

print(answer)
