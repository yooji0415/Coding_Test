import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
energy = []
for _ in range(n):
    energy.append(list(map(int, input().split())))
trees = [[{} for _ in range(n)] for _ in range(n)]
graph = [[5 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1][z] = 1


def sping_summer_winter():
    for x in range(n):
        for y in range(n):
            if trees[x][y]:
                temp = {}
                dead = 0
                for age in sorted(trees[x][y].keys()):
                    num = trees[x][y][age]
                    if graph[x][y] >= num * age:
                        graph[x][y] -= num * age
                        temp[age + 1] = num
                    else:
                        lives = graph[x][y] // age
                        dead += age // 2 * (num - lives)
                        if not lives:
                            continue
                        graph[x][y] -= age * lives
                        temp[age + 1] = lives
                graph[x][y] += dead
                trees[x][y] = temp
            graph[x][y] += energy[x][y]


directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


def fall():
    for x in range(n):
        for y in range(n):
            new_num = 0
            for age in trees[x][y].keys():
                if age % 5 == 0:
                    new_num += trees[x][y][age]
            if new_num:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if 1 not in trees[nx][ny].keys():
                            trees[nx][ny][1] = new_num
                        else:
                            trees[nx][ny][1] += new_num


for year in range(k):
    sping_summer_winter()
    fall()

answer = 0
for tree in trees:
    for t in tree:
        answer += sum(t.values())

print(answer)
