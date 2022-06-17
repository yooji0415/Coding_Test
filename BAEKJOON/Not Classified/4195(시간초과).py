import sys
from collections import deque


def bfs():
    result = 0
    queue = deque()
    queue.append(1)
    visited = [0 for _ in range(cnt + 1)]
    while queue:
        temp = queue.popleft()
        result += 1
        visited[temp] = 1
        candi = friends_graph[temp]
        for c in candi:
            if visited[c] == 0:
                queue.append(c)

    return result


tc = int(sys.stdin.readline())
for _ in range(tc):
    cnt = 1
    friends = {}
    friends_graph = {}
    friends_line_num = int(sys.stdin.readline())
    for i in range(friends_line_num):
        line = sys.stdin.readline().split()
        for friend in line:
            if friend not in friends:
                friends[friend] = cnt
                friends_graph[cnt] = []
                cnt += 1

        friends_graph[friends[line[0]]].append(friends[line[1]])
        friends_graph[friends[line[1]]].append(friends[line[0]])
        print(bfs())





