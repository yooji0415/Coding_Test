import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

combis = list(combinations([i for i in range(1, N + 1)], N // 2))

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

answer = int(1e9)
for combi in combis:
    a_team_score = 0
    b_team_score = 0
    a_team = combi
    b_team = []
    for i in range(1, N + 1):
        if i not in combi:
            b_team.append(i)

    for i in range(N // 2):
        for j in range(N // 2):
            if i == j:
                continue
            a_team_score += graph[a_team[i] - 1][a_team[j] - 1]
            b_team_score += graph[b_team[i] - 1][b_team[j] - 1]

    result = abs(a_team_score - b_team_score)
    answer = result if result < answer else answer

print(answer)
