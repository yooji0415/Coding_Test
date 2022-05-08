import sys

sys.setrecursionlimit(60000)
mem = [-1 for i in range(60001)]
# 초기에는 단순 for 문으로 dp 방법을 사용했으나
# 해당 방법으로 하면 효율성을 통과하지 못한다.
# 이는 실제 필요한 연산보다 더 많이 실행되었기 때문으로 보인다.


def dp(n):
    if mem[n] != -1: return mem[n]
    if n == 0: return 1
    if n == 1: return 1
    mem[n] = (dp(n - 1) + dp(n - 2)) % 1000000007
    return mem[n]


def solution(n):
    return dp(n)
