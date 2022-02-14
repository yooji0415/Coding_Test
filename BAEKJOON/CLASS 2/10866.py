import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0][0] == "p":
        if len(order) == 2:
            if len(order[0]) == 10:
                stack.insert(0, int(order[1]))
            else:
                stack.append(int(order[1]))
        else:
            if not stack:
                print(-1)
            else:
                if len(order[0]) == 9:
                    print(stack.pop(0))
                else:
                    print(stack.pop())
    elif order[0][0] == "s":
        print(len(stack))
    elif order[0][0] == "e":
        if not stack:
            print(1)
        else:
            print(0)
    elif order[0][0] == "f":
        if not stack:
            print(-1)
        else:
            print(stack[0])
    else:
        if not stack:
            print(-1)
        else:
            print(stack[-1])
