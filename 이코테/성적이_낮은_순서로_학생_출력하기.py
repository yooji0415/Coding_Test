n = int(input())
graph = []
for _ in range(n):
    name, score = input().split()
    graph.append((name, int(score)))

graph.sort(key=lambda x: x[1])
for i in range(n):
    print(graph[i][0], end=" ")
