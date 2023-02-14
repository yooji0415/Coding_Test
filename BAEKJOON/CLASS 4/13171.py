s = 1000000007


def find(n, s):
    return s * mul(n, s - 2) % s


def mul(b, t):
    if t == 1:
        return b % s
    if t % 2 == 0:
        temp = mul(b, t // 2)
        return (temp * temp) % s
    else:
        return b * mul(b, t - 1) % s


_sum = 0
m = int(input())
for _ in range(m):
    n, s = map(int, input().split())
    sum += find(n, s)
    sum %= s

print(_sum)
