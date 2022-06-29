import sys


num = list(map(int, list(sys.stdin.readline().strip())))
num.sort(reverse=True)
print(''.join(map(str, num)))
