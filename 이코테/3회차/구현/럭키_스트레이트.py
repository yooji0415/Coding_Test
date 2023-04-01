import sys

input = sys.stdin.readline


def solution(string):
    array = list(map(int, list(string)))
    length = len(array) // 2
    return "LUCKY" if sum(array[:length]) == sum(array[length:]) else "READY"


string = input().strip()
print(solution(string))
