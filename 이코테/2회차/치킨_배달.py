from itertools import combinations

n, m = map(int, input().split())
houses = []
chickens = []

for x in range(n):
    array = list(map(int, input().split()))
    for y in range(len(array)):
        if array[y] == 1:
            houses.append((x, y))
        if array[y] == 2:
            chickens.append((x, y))

candidate = list(combinations(chickens, m))
answer = int(1e9)
for candi in candidate:
    temp = 0
    for house in houses:
        h_x, h_y = house
        min_len = int(1e9)
        for chicken in candi:
            c_x, c_y = chicken
            min_len = min(min_len, abs(h_x - c_x) + abs(h_y - c_y))
        temp += min_len
    answer = min(answer, temp)

print(answer)
