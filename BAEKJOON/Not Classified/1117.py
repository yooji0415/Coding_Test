import sys


W, H, f, c, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

# 계산을 다 할 것이 아니라 몇 장이 겹치는지 확인한다.
# 최종 사이즈는 입력에 따라서 미리 결정할 수 있다.
if f == W:
    print(W * H - ((c + 1) * (x2 - x1)) * (y2 - y1))
elif f * 2 > W:
    print(W * H - ((c + 1) * ((W - f) - x1) * 2 + (c + 1) * (x2 - (W - f))) * (y2 - y1))
else:
    print(W * H - ((c + 1) * (f - x1) * 2 + (c + 1) * (x2 - f)) * (y2 - y1))