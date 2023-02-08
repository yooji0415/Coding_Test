# 특정 원소가 속한 집합을 찾기
def find(r, c):
    if parent[r][c] != i + "-" + j:
        [new_r, new_c] = map(int, parent[r][c].split("-"))
        return find((parent[new_r][new_c]))
    return i + "-" + j


def union(r1, c1, r2, c2):
    a = find(r1, c1)
    b = find(r2, c2)
    if a < b:
        parent[b] = a
        parent[a] = b


parent = [[0 for j in range(51)] for i in range(51)]
val_list = [[0 for j in range(51)] for i in range(51)]
for i in range(51):
    for j in range(51):
        parent[i][j] = i + "-" + j


def do_command(c):
    c_list = c.split(" ")
    command = c_list[0]
    if command == "UPDATE" and len(c_list) == 4:
        val_list[c_list[1], c_list[2]] = c_list[3]
        return
    if command == "UPDATE" and len(c_list) == 3:
        for i in range(51):
            for j in range(51):
                if val_list[i][j] == c_list[1]:
                    val_list[i][j] = c_list[2]
        return
    if command == "MERGE":
        r1, c1 = c_list[1], c_list[2]
        r2, c2 = c_list[3], c_list[4]
        if r1 == r2 and c1 == c2:
            return
        union


def solution(commands):
    answer = []
    return answer
