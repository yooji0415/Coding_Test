import sys

n = int(sys.stdin.readline())
num_set = []
for _ in range(n):
    order = sys.stdin.readline().split()
    if len(order) == 2:
        num = int(order[1])
        if order[0][0] == "a":
            if num not in num_set:
                num_set.append(num)

        elif order[0][0] == "r":
            if num not in num_set:
                continue
            else:
                num_set.remove(num)

        elif order[0][0] == "c":
            if num in num_set:
                print(1)
            else:
                print(0)

        elif order[0][0] == "t":
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.append(num)

    else:
        if order[0][0] == "a":
            num_set = list(range(1, 21))
        else:
            num_set = []
