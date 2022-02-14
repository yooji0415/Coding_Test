import sys

n = int(sys.stdin.readline())
paper = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    paper.append(temp)

cnt = [0, 0]

def paper_count(x, y, N, cnt):
  color = paper[x][y]
  for i in range(x, x+N):
    for j in range(y, y+N):
      if color != paper[i][j]:
        paper_count(x, y, N//2, cnt)
        paper_count(x, y+N//2, N//2, cnt)
        paper_count(x+N//2, y, N//2, cnt)
        paper_count(x+N//2, y+N//2, N//2, cnt)
        return
  if color == 0:
    cnt[0] += 1
  else :
    cnt[1] += 1


paper_count(0, 0, n, cnt)
print(cnt[0])
print(cnt[1])
