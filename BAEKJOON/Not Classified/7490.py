import sys
from itertools import product


tc = int(sys.stdin.readline())
for _ in range(tc):
    n = int(sys.stdin.readline())
    n_list = [x for x in range(1, n + 1)]
    for operator in product([' ', '+', '-'], repeat=n - 1):
        result = str(n_list[0])
        answer = str(n_list[0])
        for i, o in enumerate(operator):
            if o == ' ':
                result += str(n_list[i + 1])
            else:
                result += o + str(n_list[i + 1])

            answer += o + str(n_list[i + 1])

        if eval(result) == 0:
            print(answer)

    print()
    