import sys
import math

# n은 2의 차수 r은 행 c는 열
n, r, c = map(int, sys.stdin.readline().split())
cnt = 0

while n > 0:
    n -= 1
    # 좌상단
    if r < 2**n and c < 2**n:
       continue
    # 우상단
    elif r < 2**n and c >= 2**n:
        cnt += 2**n * 2**n
        c -= 2**n
    # 좌하단
    elif r >= 2**n and c < 2**n:
        cnt += 2**n * 2**n * 2
        r -= 2**n
    # 우하단
    else:
        cnt += 2**n * 2**n * 3
        r -= 2**n
        c -= 2**n

print(cnt)
