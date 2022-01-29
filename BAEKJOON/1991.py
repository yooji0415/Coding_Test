import sys


def printer(node, pos, mode):
    if mode == 0:
        print(pos, end="")
        if node[pos][0] != ".":
            printer(node, node[pos][0], mode)
        if node[pos][1] != ".":
            printer(node, node[pos][1], mode)
    elif mode == 1:
        if node[pos][0] != ".":
            printer(node, node[pos][0], mode)
        print(pos, end="")
        if node[pos][1] != ".":
            printer(node, node[pos][1], mode)
    else:
        if node[pos][0] != ".":
            printer(node, node[pos][0], mode)
        if node[pos][1] != ".":
            printer(node, node[pos][1], mode)
        print(pos, end="")


n = int(sys.stdin.readline())
node = {}
for _ in range(n):
    p, l, r = sys.stdin.readline().split()
    node[p] = [l, r]

printer(node, "A", 0)
print()
printer(node, "A", 1)
print()
printer(node, "A", 2)
print()
