global answer
answer = 0


def dfs(idx, visited):
    global answer
    if False not in visited:
        answer += 1
        return

    for i in range(idx, len(visited)):
        


c = int(input())
for _ in range(c):
    # 학생수 N 친구 쌍 수 M
    [n, m] = map(int, input().split(" "))
    pair_list = []
    pair_input = map(int, input().split(" "))
    for i in range(len(pair_input)):
        if i % 2 != 0:
            continue
        pair_list.append([pair_input[i], pair_input[i+1]])


