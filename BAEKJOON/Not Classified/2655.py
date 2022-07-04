import sys


# 벽돌의 개수를 받는다.
n = int(sys.stdin.readline())
# 맨 앞에 더미를 하나 넣은 블록 리스트 생성
blocks = [(0, 0, 0, 0)]
# 블록의 값을 받는다.
for i in range(1, n + 1):
    b, h, w = map(int, sys.stdin.readline().split())
    blocks.append((i, b, h, w))

# 기준이 두 가지 이니 하나인 무게로 일단 정렬
# 이때 오름차순으로 정렬한다.
blocks.sort(key=lambda x: x[3])

dp = [0] * (n + 1)
# 한 칸씩 늘려가며 반복 진행한다.
for i in range(1, n + 1):
    for j in range(0, i):
        # 만약 블록의 너비가 더 크다면 쌓을 수 있다.
        if blocks[i][1] > blocks[j][1]:
            dp[i] = max(dp[i], dp[j] + blocks[i][2])

max_height = max(dp)
index = n
result = []
# 역추적 하면서 쌓은 경로를 찾아낸다.
while index != 0:
    if max_height == dp[index]:
        result.append(blocks[index][0])
        max_height -= blocks[index][2]
    index -= 1

result.reverse()
print(len(result))
[print(i) for i in result]
