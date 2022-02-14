import sys

cycle = int(sys.stdin.readline())
fibo_count = {
    0: [1, 0],
    1: [0, 1]
}


def fibo(num):
    for n in range(2, num+1):
        fibo_count[n] = [fibo_count[n-2][0] + fibo_count[n-1][0],
                   fibo_count[n-2][1] + fibo_count[n-1][1]]

for _ in range(cycle):
    n = int(sys.stdin.readline())
    fibo(40)
    print("{} {}".format(fibo_count[n][0], fibo_count[n][1]))
