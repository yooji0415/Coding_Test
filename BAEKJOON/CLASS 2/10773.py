import sys

K = int(sys.stdin.readline().strip())
stack = []
for _ in range(K):
    N = int(sys.stdin.readline().strip())
    if N != 0:
        stack.append(N)
    else:
        if not stack:
            print(0)
            break
        else:
            stack.pop()

print(sum(stack))