import sys

test = int(sys.stdin.readline())
for _ in range(test):
    sticker = []
    n = int(sys.stdin.readline())
    for _ in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))

    for i in range(1, n):
        if i == 1:
            sticker[0][1] = sticker[1][0] + sticker[0][1]
            sticker[1][1] = sticker[0][0] + sticker[1][1]
        else:
            sticker[0][i] = max(sticker[1][i-1], sticker[1][i-2]) + sticker[0][i]
            sticker[1][i] = max(sticker[0][i-1], sticker[0][i-2]) + sticker[1][i]

    print(max(sticker[0][n-1], sticker[1][n-1]))