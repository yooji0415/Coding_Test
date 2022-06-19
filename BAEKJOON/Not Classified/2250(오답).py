import sys


def inorder(num, y):
    if tree[num][0] != -1:
        inorder(tree[num][0], y + 1)
    x_level.append(num)
    if y not in y_level:
        y_level[y] = []
    y_level[y].append(num)
    if tree[num][1] != -1:
        inorder(tree[num][1], y + 1)


n = int(sys.stdin.readline())
tree = {}
for _ in range(n):
    p, l, r = map(int, sys.stdin.readline().split())
    tree[p] = [l, r]

x_level = []
y_level = {}
inorder(1, 1)
answer_level = 0
answer_len = 0

for level, nodes in sorted(y_level.items()):
    a_x = x_level.index(nodes[0])
    b_x = x_level.index(nodes[-1])
    if answer_len < b_x - a_x + 1:
        answer_level = level
        answer_len = b_x - a_x + 1

print(f"{answer_level} {answer_len}")
