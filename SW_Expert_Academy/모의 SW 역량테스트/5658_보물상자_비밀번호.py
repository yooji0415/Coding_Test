T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    A = list(input())
    turn = N//4
    result = 0
    L = []
    for _ in range(turn):
        for i in range(0, N, turn):
            temp = int(''.join(A[i:i+turn]), 16)
            if temp not in L:
                L.append(temp)
        A = [A[-1]] + A[:-1]
    print("#{} {}".format(tc+1, sorted(L, reverse=True)[K-1]))