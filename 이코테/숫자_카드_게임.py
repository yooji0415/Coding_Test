n, m = map(int, input().split())
min_num_per_lint = []
for i in range(n):
    line_data = list(map(int, input().split()))
    min_num_per_lint.append(min(line_data))

print(max(min_num_per_lint))
