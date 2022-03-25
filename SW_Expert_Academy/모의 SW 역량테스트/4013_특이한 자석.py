T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    W = []
    for _ in range(4):
        temp = list(map(int, input().split()))
        W.append(temp)

    # W의 0번 인덱스가 top, 2번 인덱스가 right, -2번 인덱스가 left
    for _ in range(K):
        q = []
        info = [0, 0, 0, 0]
        N, R = map(int, input().split())
        q.append(N - 1)
        info[N - 1] = R
        while q:
            temp = q.pop(0)
            C = [temp - 1, temp + 1]
            for i in range(2):
                if C[i] > 3 or C[i] < 0:
                    continue

                if i == 0 and W[temp][-2] != W[C[i]][2] and info[C[i]] == 0:
                    info[C[i]] = - info[temp]
                    q.append(C[i])

                elif i == 1 and W[temp][2] != W[C[i]][-2] and info[C[i]] == 0:
                    info[C[i]] = - info[temp]
                    q.append(C[i])

        for i in range(4):
            if info[i] == 0:
                continue

            if info[i] == 1:
                W[i] = [W[i][-1]] + W[i][:-1]
            elif info[i] == -1:
                W[i] = W[i][1:] + [W[i][0]]

    print("#{} {}".format(tc, W[0][0] + W[1][0] * 2 + W[2][0] * 4 + W[3][0] * 8))
