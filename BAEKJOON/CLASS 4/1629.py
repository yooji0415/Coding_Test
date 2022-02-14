import sys


def find_answer(a, b, c):
    if b == 1:
        return a % c
    else:
        temp = find_answer(a, b//2, c)
        if b % 2 == 1:
            return temp * temp * a % c
        else:
            return temp * temp % c


a, b, c = map(int, sys.stdin.readline().split())
answer = find_answer(a, b, c)
print(answer)
