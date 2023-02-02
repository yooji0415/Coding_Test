n = int(input())
graph = []

for _ in range(n):
    graph.append(int(input()))

graph.sort(reverse=True)
graph = map(str, graph)
print(" ".join(graph))
