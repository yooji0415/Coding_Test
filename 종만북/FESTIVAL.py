import sys

c = int(sys.stdin.readline())
for _ in range(c):
    n, l = list(map(int, sys.stdin.readline().split()))
    costs = list(map(int, sys.stdin.readline().split()))
    min_cost = 10000
    while l <= len(costs):
        s_idx = 0
        e_idx = l - 1
        total = sum(costs[s_idx: e_idx + 1])
        ever = total / l
        min_cost = ever if ever < min_cost else min_cost
        while e_idx < len(costs) - 1:
            total = total - costs[s_idx] + costs[e_idx + 1]
            ever = total / l
            min_cost = ever if ever < min_cost else min_cost
            s_idx += 1
            e_idx += 1

        l += 1

    print(min_cost)

