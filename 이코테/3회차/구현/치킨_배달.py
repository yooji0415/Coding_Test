from itertools import combinations

N, M = map(int, input().split())
chickens = []
houses = []
for x in range(N):
    array = list(map(int, input().split()))
    for y in range(N):
        if array[y] == 1:
            houses.append((x, y))
        elif array[y] == 2:
            chickens.append((x, y))


def calc_chicken_cost(chickens, houses):
    answer = 0
    for house in houses:
        cost = int(1e9)
        for chicken in chickens:
            cost = min(cost, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        answer += cost
    return answer


answer = int(1e9)
for combi in combinations(chickens, M):
    result = calc_chicken_cost(combi, houses)
    answer = min(result, answer)

print(answer)
