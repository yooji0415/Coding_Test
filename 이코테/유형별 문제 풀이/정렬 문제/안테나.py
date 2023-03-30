n = int(input())
points = list(map(int, input().split()))

points.sort()
min_sum = int(1e9)
answer = 0

for i in range(n):
    left = points[:i]
    right = points[i:]
    now_point = points[i]
    total = now_point * len(left) - sum(left) + sum(right) - now_point * len(right)
    # print(f"{i} 인덱스 토탈: {total}")
    if min_sum > total:
        min_sum = total
        answer = now_point

print(answer)
